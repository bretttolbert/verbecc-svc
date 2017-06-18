from __future__ import print_function

from .conjugations_parser import ConjugationsParser
from .mood import Mood
from .person import Person
from .template import Template
from .tense import Tense
from .verb import Verb
from .verbs_parser import VerbsParser


class Conjugator:
    def __init__(self):
        self.vp = VerbsParser()
        self.cp = ConjugationsParser()

    def conjugate_verb(self, infinitive):
        verb = self.vp.find_verb_by_infinitive(infinitive)
        print(verb.infinitive)
        template = self.cp.find_template(verb.template)
        print(repr(template))
        mood = template.moods['indicative']
        tense = mood.tenses['present']
