from __future__ import print_function

from .conjugations_parser import ConjugationsParser
from .mood import Mood
from .person import Person
from .template import Template
from .tense import Tense
from .verb import Verb
from .verbs_parser import (
    VerbNotFoundError, VerbsParser
)


class ConjugatorError(Exception):
    pass


class Conjugator:
    def __init__(self):
        self.vp = VerbsParser()
        self.cp = ConjugationsParser()

    def conjugate(self, infinitive):
        ret = ""
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
        ret += self._conjugate_specific_mood_tense(verb_stem, mood, tense)
        tense = mood.tenses['imperfect']
        ret += self._conjugate_specific_mood_tense(verb_stem, mood, tense)
        tense = mood.tenses['future']
        ret += self._conjugate_specific_mood_tense(verb_stem, mood, tense)
        tense = mood.tenses['simple-past']
        ret += self._conjugate_specific_mood_tense(verb_stem, mood, tense)
        return ret

    def _conjugate_specific_mood_tense(self, verb_stem, mood, tense):
        ret = '\n{}\n'.format(tense.name)
        for pronoun in ('je', 'tu', 'il', 'nous', 'vous', 'ils'):
            person = tense.find_person_by_pronoun(pronoun)
            ending = person.get_ending()
            if pronoun == 'je' and verb_stem.startswith('a'):
                ret += "j'"
            else:
                ret += '{} '.format(pronoun)
            ret += u'{}{}\n'.format(verb_stem, ending)
        ret += '\n'
        return ret
