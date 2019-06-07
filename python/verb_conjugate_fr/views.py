#!/usr/bin/env python
from verb_conjugate_fr import app
from fastapi import HTTPException
from .conjugator import Conjugator, get_verb_stem, InvalidMoodError
from .conjugation_template import ConjugationTemplate
from .conjugations_parser import ConjugationsParser, TemplateNotFoundError
from .verbs_parser import VerbsParser, VerbNotFoundError

cg = Conjugator()

@app.get("/")
def read_root():
    return {'value': 'Hello 世界'}

@app.get("/conjugate/{infinitive}")
def read_conjugation(infinitive: str):
    value = None
    try:
        value = cg.conjugate(infinitive)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except InvalidMoodError:
        raise HTTPException(status_code=404, detail="Invalid mood")
    except TemplateNotFoundError:
        raise HTTPException(status_code=404, detail="Template not found")
    except ConjugatorError:
        raise HTTPException(status_code=404, detail="Conjugator error")
    except:
        raise HTTPException(status_code=404, detail="Unknown error")
    return {'value': value}

@app.get("/find/infinitive/{infinitive}")
def read_find_infinitive(infinitive: str):
    value = None
    try:
        value = cg.verb_parser.find_verb_by_infinitive(infinitive)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except:
        raise HTTPException(status_code=404, detail="Unknown error")
    return {'value': value}

@app.get("/find/conjugation-template/{template_name}")
def read_find_conjugation_template(template_name: str):
    value = None
    try:
        value = cg.conj_parser.find_template(template_name)
    except TemplateNotFoundError:
        raise HTTPException(status_code=404, detail="Template not found")
    except:
        raise HTTPException(status_code=404, detail="Unknown error")
    return {'value': value}

@app.get("/conjugate/mood/{mood}/{infinitive}")
def read_conjugation_for_mood(mood: str, infinitive: str):
    value = None
    try:
        verb = cg.verb_parser.find_verb_by_infinitive(infinitive)
        verb_stem = get_verb_stem(infinitive, verb.template)
        template = cg.conj_parser.find_template(verb.template)
        value = cg.get_full_conjugation_for_mood(verb_stem, template, mood)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except InvalidMoodError:
        raise HTTPException(status_code=404, detail="Invalid mood")
    except:
        raise HTTPException(status_code=404, detail="Unknown error")
    return {'value': value}
