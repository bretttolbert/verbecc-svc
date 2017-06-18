# -*- coding: utf-8 -*-

from __future__ import print_function

from .conjugations_parser import ConjugationsParser
from .mood import Mood
from .person import Person
from .string_utils import (
    starts_with_vowel,
    strip_accents
)
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
        print(u'Conjugaison du verbe {}'.format(verb.infinitive))
        template = self.cp.find_template(verb.template)
        print(u"Template: {}".format(template.name))
        verb_stem = get_verb_stem(infinitive, template.name)
        mood = template.moods['indicative']
        tense = mood.tenses['present']
        ret += conjugate_specific_tense(verb_stem, tense)
        tense = mood.tenses['imperfect']
        ret += conjugate_specific_tense(verb_stem, tense)
        tense = mood.tenses['future']
        ret += conjugate_specific_tense(verb_stem, tense)
        tense = mood.tenses['simple-past']
        ret += conjugate_specific_tense(verb_stem, tense)
        return ret


def get_verb_stem(infinitive, template_name):
    template_beg, template_ending = template_name.split(u':')
    if not infinitive.endswith(template_ending):
        raise ConjugatorError(
            "Template {} ending doesn't "
            "match infinitive {}"
            .format(template_name, infinitive))
    return infinitive[:len(infinitive) - len(template_ending)]


def conjugate_specific_tense(verb_stem, tense):
    ret = '{}\n'.format(tense.name)
    for pronoun in ('je', 'tu', 'il', 'nous', 'vous', 'ils'):
        person = tense.find_person_by_pronoun(pronoun)
        ret += conjugate_specific_tense_pronoun(verb_stem, person, pronoun)
        ret += '\n'
    ret += '\n'
    return ret


def conjugate_specific_tense_pronoun(verb_stem, person, pronoun):
    ret = ''
    ending = person.get_ending()
    conjugated_verb = verb_stem + ending
    if pronoun == 'je' and starts_with_vowel(conjugated_verb):
        ret += "j'"
    else:
        ret += pronoun + ' '
    ret += u'{}'.format(conjugated_verb)
    return ret
