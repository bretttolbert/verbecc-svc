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


def cli_try_conjugate(conjugator, verb):
    try:
        conjugator.conjugate(verb)
    except VerbNotFoundError:
        print("Aucune mot trouvé")
        print("Verb not found")
        matches = conjugator.vp.get_verbs_that_start_with(verb)
        if len(matches):
            print('Matches:')
            for match in matches:
                print(u'{}'.format(match.infinitive))
        else:
            print('No matches')


def main():
    conjugator = Conjugator()
    if len(sys.argv) > 1:
        verb = sys.argv[1]
        cli_try_conjugate(conjugator, verb)
    while True:
        print("Entrez un mot français pour conjuguer")
        print("Enter a French verb to conjugate")
        verb = input()
        if verb == 'exit':
            return
        cli_try_conjugate(conjugator, verb)
