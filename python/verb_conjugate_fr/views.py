#!/usr/bin/env python
from verb_conjugate_fr import app
from .conjugator import Conjugator
from .conjugation_template import ConjugationTemplate
from .conjugations_parser import ConjugationsParser
from .verbs_parser import VerbsParser, VerbNotFoundError

@app.get("/")
def read_root():
    return {'value': 'Hello 世界'}

@app.get("/conjugate/{infinitive}")
def read_conjugation(infinitive: str):
    conjugator = Conjugator()
    out = conjugator.get_full_conjugation_string(infinitive)
    return {'value': out}

@app.get("/find/infinitive/{infinitive}")
def read_find_infinitive(infinitive: str):
    verb_parser = VerbsParser()
    verb = verb_parser.find_verb_by_infinitive(infinitive)
    return {'value': verb}
