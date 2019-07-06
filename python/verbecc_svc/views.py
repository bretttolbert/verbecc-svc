#!/usr/bin/env python
from verbecc_svc import app
from fastapi import HTTPException
import sys
import traceback
from verbecc.conjugator import (
    Conjugator, 
    ConjugatorError, 
    InvalidMoodError,
    TemplateNotFoundError,
    VerbNotFoundError)

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
        extype, exval, extb = sys.exc_info()
        raise HTTPException(status_code=404, 
            detail="Error: {}\nTraceback: {}".format(
                exval, traceback.format_tb(extb)))
    return {'value': value}

@app.get("/search/infinitive/{query}")
def read_search_infinitive(query: str, max_results=10):
    matches = cg.get_verbs_that_start_with(query, max_results);
    return {'value': matches}

@app.get("/find/infinitive/{infinitive}")
def read_find_infinitive(infinitive: str):
    value = None
    try:
        value = cg.find_verb_by_infinitive(infinitive)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except:
        extype, exval, extb = sys.exc_info()
        raise HTTPException(status_code=404, 
            detail="Error: {}\nTraceback: {}".format(
                exval, traceback.format_tb(extb)))
    return {'value': value}

@app.get("/find/conjugation-template/{template_name}")
def read_find_conjugation_template(template_name: str):
    value = None
    try:
        value = cg.find_template(template_name)
    except TemplateNotFoundError:
        raise HTTPException(status_code=404, detail="Template not found")
    except:
        extype, exval, extb = sys.exc_info()
        raise HTTPException(status_code=404, 
            detail="Error: {}\nTraceback: {}".format(
                exval, traceback.format_tb(extb)))
    return {'value': value}

@app.get("/conjugate/mood/{mood}/{infinitive}")
def read_conjugation_for_mood(mood: str, infinitive: str):
    value = None
    try:
        value = cg.get_full_conjugation_for_mood(infinitive, mood)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except InvalidMoodError:
        raise HTTPException(status_code=404, detail="Invalid mood")
    except:
        extype, exval, extb = sys.exc_info()
        raise HTTPException(status_code=404, 
            detail="Error: {}\nTraceback: {}".format(
                exval, traceback.format_tb(extb)))
    return {'value': value}

@app.get("/conjugate/{infinitive}/passe-compose")
def read_conjugation_passe_compose(infinitive: str):
    value = None
    try:
        value = cg.conjugate_passe_compose(infinitive)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except InvalidMoodError:
        raise HTTPException(status_code=404, detail="Invalid mood")
    except:
        extype, exval, extb = sys.exc_info()
        raise HTTPException(status_code=404, 
            detail="Error: {}\nTraceback: {}".format(
                exval, traceback.format_tb(extb)))
    return {'value': value}
