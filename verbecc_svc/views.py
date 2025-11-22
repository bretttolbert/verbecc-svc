#!/usr/bin/env python
import sys
import traceback
from functools import partial

from fastapi import HTTPException

from verbecc_svc import app

from verbecc import CompleteConjugator, grammar_defines
from verbecc import Mood, Tense
from verbecc import (
    VerbNotFoundError,
    InvalidLangError,
    InvalidMoodError,
    InvalidTenseError,
    TemplateNotFoundError,
    ConjugatorError,
)

conjugators = {
    lang: CompleteConjugator(lang=lang) for lang in grammar_defines.SUPPORTED_LANGUAGES
}


def cg(lang):
    if lang in conjugators:
        return conjugators[lang]
    else:
        raise HTTPException(status_code=404, detail="Invalid language")


@app.get("/")
def root():
    return return_data("Hello 世界")


@app.get("/supported-langs")
def supported_langs():
    return return_data(grammar_defines.SUPPORTED_LANGUAGES)


@app.get("/conjugate/{lang}/{infinitive}")
def conjugate(lang: str, infinitive: str, mood: str = "all", tense: str = "all"):
    ret = None
    try:
        cc = cg(lang).conjugate(infinitive)
        ret = cc
        if mood != "all":
            mc = cc.get_moods()[Mood(mood)]
            ret = mc
            if tense != "all":
                tc = cg(lang).conjugate_mood_tense(infinitive, Mood(mood), Tense(tense))
                ret = tc
        return return_data(ret.get_data())
    except Exception as exc:
        handle_error(exc)


@app.get("/search/infinitive/{lang}/{query}")
def search_infinitive(lang: str, query: str, max_results=10):
    try:
        return return_data(cg(lang).get_verbs_that_start_with(query, max_results))
    except Exception as exc:
        handle_error(exc)


@app.get("/find/infinitive/{lang}/{infinitive}")
def find_infinitive(lang: str, infinitive: str):
    try:
        return return_data(cg(lang).find_verb_by_infinitive(infinitive))
    except Exception as exc:
        handle_error(exc)


@app.get("/find/template/{lang}/{template}")
def find_template(lang: str, template: str):
    try:
        return return_data(cg(lang).find_template(template))
    except Exception as exc:
        handle_error(exc)


def return_data(value):
    return {"value": value}


def handle_error(exc):
    if isinstance(VerbNotFoundError, exc):
        raise HTTPException(status_code=404, detail="Verb not found")
    elif isinstance(InvalidLangError, exc):
        raise HTTPException(status_code=404, detail="Invalid language")
    elif isinstance(InvalidMoodError, exc):
        raise HTTPException(status_code=404, detail="Invalid mood")
    elif isinstance(InvalidTenseError, exc):
        raise HTTPException(status_code=404, detail="Invalid tense")
    elif isinstance(TemplateNotFoundError, exc):
        raise HTTPException(status_code=404, detail="Template not found")
    elif isinstance(ConjugatorError, exc):
        raise HTTPException(status_code=404, detail="Conjugator error")
    else:
        extype, exval, extb = sys.exc_info()
        raise HTTPException(
            status_code=404,
            detail="Error: {}\nTraceback: {}".format(exval, traceback.format_tb(extb)),
        )
