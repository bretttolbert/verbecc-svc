# -*- coding: utf-8 -*-

from __future__ import print_function

from .conjugation_template import ConjugationTemplate
from .conjugations_parser import ConjugationsParser
from . import grammar_defines
from .mood import Mood
from .person_ending import PersonEnding
from .string_utils import (
    starts_with_vowel,
    strip_accents
)
from .tense_template import TenseTemplate
from .verb import Verb
from .verbs_parser import (
    VerbNotFoundError, VerbsParser
)


class ConjugatorError(Exception):
    pass


def get_verb_stem(infinitive, template_name):
    template_beg, template_ending = template_name.split(u':')
    if not infinitive.endswith(template_ending):
        raise ConjugatorError(
            "Template {} ending doesn't "
            "match infinitive {}"
            .format(template_name, infinitive))
    return infinitive[:len(infinitive) - len(template_ending)]


class Conjugator:
    def __init__(self):
        self.verb_parser = VerbsParser()
        self.conj_parser = ConjugationsParser()

    def conjugate(self, infinitive):
        ret = {'moods': {'indicative': []}}
        verb = self.verb_parser.find_verb_by_infinitive(infinitive)
        print(u'Conjugaison du verbe "{}":'.format(verb.infinitive))
        conjugation_template = self.conj_parser.find_template(verb.template)
        print(u"Conjugation template: {}".format(conjugation_template.name))
        verb_stem = get_verb_stem(infinitive, conjugation_template.name)
        ret['moods']['indicative'] = self._get_full_conjugation_for_mood(verb_stem, conjugation_template, 'indicative')
        return ret

    def get_full_conjugation_string(self, infinitive):
        ret = ''
        verb = self.verb_parser.find_verb_by_infinitive(infinitive)
        print(u'Conjugaison du verbe "{}":'.format(verb.infinitive))
        conjugation_template = self.conj_parser.find_template(verb.template)
        print(u"Conjugation template: {}".format(conjugation_template.name))
        verb_stem = get_verb_stem(infinitive, conjugation_template.name)
        return self._get_full_conjugation_string_for_mood(verb_stem, conjugation_template, 'indicative')

    def _get_full_conjugation_for_mood(self, verb_stem, template, mood_name):
        ret = {}
        mood = template.moods[mood_name]

        for tense in ('present', 'imperfect', 'future', 'simple-past'):
            tense_template = mood.tenses[tense]
            ret[tense] = self._conjugate_specific_tense(verb_stem, tense_template)
        return ret

    def _get_full_conjugation_string_for_mood(self, verb_stem, template, mood_name):
        ret = ''
        mood = template.moods[mood_name]

        for tense in ('present', 'imperfect', 'future', 'simple-past'):
            tense_template = mood.tenses[tense]
            ret += tense + '\n'
            ret += '\n'.join(self._conjugate_specific_tense(verb_stem, tense_template))
            ret += '\n'

        # mood = template.moods['participle']
        # tense = mood.tenses['present-participle']
        # ret += self._conjugate_specific_tense(verb_stem, tense)
        return ret

    def _conjugate_specific_tense(self, verb_stem, tense_template):
        ret = []
        for pronoun in grammar_defines.get_default_pronouns():
            person = tense_template.get_person_ending_by_pronoun(pronoun)
            ending = person.get_ending()
            ret.append(self._conjugate_specific_tense_pronoun(verb_stem, ending, pronoun))
        return ret

    def _conjugate_specific_tense_pronoun(self, verb_stem, ending, pronoun):
        ret = u''
        conjugated_verb = verb_stem + ending
        if pronoun == 'je' and starts_with_vowel(conjugated_verb):
            ret += u"j'"
        else:
            ret += pronoun + ' '
        ret += u'{}'.format(conjugated_verb)
        return ret
