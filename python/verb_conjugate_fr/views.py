#!/usr/bin/env python
from verb_conjugate_fr import app
from fastapi import HTTPException
from .conjugator import Conjugator, get_verb_stem
from .conjugation_template import ConjugationTemplate
from .conjugations_parser import ConjugationsParser
from .verbs_parser import VerbsParser, VerbNotFoundError

cg = Conjugator()

@app.get("/")
def read_root():
    return {'value': 'Hello 世界'}

@app.get("/conjugate/{infinitive}")
def read_conjugation(infinitive: str):
    out = cg.get_full_conjugation_string(infinitive)
    return {'value': out}

@app.get("/find/infinitive/{infinitive}")
def read_find_infinitive(infinitive: str):
    value = None
    try:
        value = cg.verb_parser.find_verb_by_infinitive(infinitive)
    except VerbNotFoundError:
        raise HTTPException(status_code=404, detail="Verb not found")
    return {'value': value}

@app.get("/find/conjugation-template/{template_name}")
def read_find_conjugation_template(template_name: str):
    template = cg.conj_parser.find_template(template_name)
    return {'value': template}

@app.get("/conjugate/mood/{mood}/{infinitive}")
def read_conjugation_for_mood(mood: str, infinitive: str):
    verb = cg.verb_parser.find_verb_by_infinitive(infinitive)
    verb_stem = get_verb_stem(infinitive, verb.template)
    template = cg.conj_parser.find_template(verb.template)
    value = cg._get_full_conjugation_for_mood(verb_stem, template, mood)
    return {'value': value}
