#!/usr/bin/env python
import sys
import traceback
from functools import partial

from fastapi import HTTPException

from verbecc_svc import app

from verbecc import conjugator
from verbecc import exceptions

conjugators = {lang : conjugator.Conjugator(lang=lang) 
               for lang in conjugator.SUPPORTED_LANGUAGES}

def cg(lang):
    if lang in conjugators:
        return conjugators[lang]
    else:
        raise HTTPException(status_code=404, detail="Invalid language")

@app.get("/")
def root():
    return {'value': 'Hello 世界'}

@app.get("/supported-langs")
def supported_langs():
    return {'value': conjugator.SUPPORTED_LANGUAGES}

@app.get("/conjugate/{lang}/{infinitive}")
def conjugate(lang: str, infinitive: str, mood: str = 'all', tense: str = 'all'):
    op = partial(cg(lang).conjugate, infinitive)
    if mood is not 'all':
        op = partial(cg(lang).conjugate_mood, infinitive, mood)
        if tense is not 'all':
            op = partial(cg(lang).conjugate_mood_tense, infinitive, mood, tense)
    return do_op(op)

@app.get("/search/infinitive/{lang}/{query}")
def search_infinitive(lang: str, query: str, max_results=10):
    return do_op(partial(cg(lang).get_verbs_that_start_with, query, max_results))

@app.get("/find/infinitive/{lang}/{infinitive}")
def find_infinitive(lang: str, infinitive: str):
    return do_op(partial(cg(lang).find_verb_by_infinitive, infinitive))

@app.get("/find/template/{lang}/{template}")
def find_template(lang: str, template: str):
    return do_op(partial(cg(lang).find_template, template))

def do_op(op):
    value = None
    try:
        value = op()
    except exceptions.VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    except exceptions.InvalidLangError:
        raise HTTPException(status_code=404, detail="Invalid language")
    except exceptions.InvalidMoodError:
        raise HTTPException(status_code=404, detail="Invalid mood")
    except exceptions.InvalidTenseError:
        raise HTTPException(status_code=404, detail="Invalid tense")
    except exceptions.TemplateNotFoundError:
        raise HTTPException(status_code=404, detail="Template not found")
    except exceptions.ConjugatorError:
        raise HTTPException(status_code=404, detail="Conjugator error")
    except:
        extype, exval, extb = sys.exc_info()
        raise HTTPException(status_code=404, 
            detail="Error: {}\nTraceback: {}".format(
                exval, traceback.format_tb(extb)))
    return {'value': value}
