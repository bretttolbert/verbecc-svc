import sys

from .conjugator import Conjugator
from .verbs_parser import (
    VerbNotFoundError
)


# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass


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
