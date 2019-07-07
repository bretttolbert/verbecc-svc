#!/usr/bin/env python
import sys
import traceback
from functools import partial

from fastapi import HTTPException

from verbecc_svc import app

from verbecc import conjugator
from verbecc import exceptions

cg = conjugator.Conjugator()

@app.get("/")
def read_root():
    return {'value': 'Hello 世界'}

@app.get("/conjugate/{infinitive}")
def conjugate(infinitive: str, mood: str = 'all', tense: str = 'all'):
    op = partial(cg.conjugate, infinitive)
    if mood is not 'all':
        op = partial(cg.conjugate_mood, infinitive, mood)
        if tense is not 'all':
            op = partial(cg.conjugate_mood_tense, infinitive, mood, tense)
    return do_op(op)

@app.get("/search/infinitive/{query}")
def search_infinitive(query: str, max_results=10):
    return do_op(partial(cg.get_verbs_that_start_with, query, max_results))

@app.get("/find/infinitive/{infinitive}")
def find_infinitive(infinitive: str):
    return do_op(partial(cg.find_verb_by_infinitive, infinitive))

@app.get("/find/conjugation-template/{template_name}")
def find_conjugation_template(template_name: str):
    return do_op(partial(cg.find_template, template_name))

def do_op(op):
    value = None
    try:
        value = op()
    except exceptions.VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
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
