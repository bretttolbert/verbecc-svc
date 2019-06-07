#!/usr/bin/env python
from verb_conjugate_fr import app, api
from flask_restful import Resource
from .conjugator import Conjugator
from .verbs_parser import VerbNotFoundError

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Conjugate(Resource):
    def __init__(self):
        self.conjugator = Conjugator()

    def get(self, infinitive):
        out = self.conjugator.get_full_conjugation_string(infinitive)
        return {'conjugation': out}

api.add_resource(HelloWorld, '/')
api.add_resource(Conjugate, '/<string:infinitive>')
