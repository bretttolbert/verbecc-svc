#!/usr/bin/env python
from verb_conjugate_fr import app
from .conjugator import Conjugator
from .verbs_parser import VerbNotFoundError

@app.get("/")
def read_root():
    return {'hello': '世界'}

@app.get("/conjugate/{infinitive}")
def read_conjugation(infinitive: str):
    conjugator = Conjugator()
    out = conjugator.get_full_conjugation_string(infinitive)
    return {'conjugation': out}
