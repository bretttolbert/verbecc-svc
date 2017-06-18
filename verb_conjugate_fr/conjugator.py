from __future__ import print_function

import sys

from .conjugations_parser import ConjugationsParser
from .mood import Mood
from .person import Person
from .template import Template
from .tense import Tense
from .verb import Verb
from .verbs_parser import (
    VerbNotFoundError, VerbsParser
)


# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass


class ConjugatorError(Exception):
    pass


class Conjugator:
    def __init__(self):
        self.vp = VerbsParser()
        self.cp = ConjugationsParser()

    def conjugate(self, infinitive):
        verb = self.vp.find_verb_by_infinitive(infinitive)
        print('Conjugaison du verbe {}'.format(verb.infinitive))
        template = self.cp.find_template(verb.template)
        print("Template: {}".format(template.name))
        template_beg, template_ending = template.name.split(':')
        if not infinitive.endswith(template_ending):
            raise ConjugatorError(
                "Template {} ending doesn't "
                "match infinitive {}"
                .format(template.name, infinitive))
        verb_stem = infinitive[:len(infinitive)-len(template_ending)]
        mood = template.moods['indicative']
        tense = mood.tenses['present']
        print('')
        for pronoun in ('je', 'tu', 'il', 'nous', 'vous', 'ils'):
            person = tense.find_person_by_pronoun(pronoun)
            ending = person.get_ending()
            if pronoun == 'je' and verb_stem.startswith('a'):
                print('j\'{}{}'.format(verb_stem, ending))
            else:
                print('{} {}{}'.format(pronoun, verb_stem, ending))
        print('')


def main():
    conjugator = Conjugator()
    if len(sys.argv) > 1:
        conjugator.conjugate(sys.argv[1])
    while True:
        print("Entrez un mot français pour conjuguer")
        print("Enter a French verb to conjugate")
        verb = input()
        if input == 'exit' or input.startswith('quit'):
            return
        try:
            conjugator.conjugate(verb)
        except VerbNotFoundError:
            print("Aucune mot trouvé")
            print("Verb not found")
