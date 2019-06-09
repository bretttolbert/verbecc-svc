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

class InvalidMoodError(Exception):
    pass

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

def prepend_with_que(pronoun_string):
    if starts_with_vowel(pronoun_string):
        return "qu'" + pronoun_string
    else:
        return "que " + pronoun_string

TENSES_CONJUGATED_WITHOUT_PRONOUNS = ['infinitive-present', 'present-participle', 
                                      'imperative-present', 'past-participle']

class Conjugator:
    def __init__(self):
        self.verb_parser = VerbsParser()
        self.conj_parser = ConjugationsParser()

    def conjugate(self, infinitive):
        verb = self.verb_parser.find_verb_by_infinitive(infinitive)
        conjugation_template = self.conj_parser.find_template(verb.template)
        verb_stem = get_verb_stem(verb.infinitive, conjugation_template.name)
        moods = {}
        for mood in conjugation_template.moods:
            moods[mood] = self.get_full_conjugation_for_mood(
            verb_stem, conjugation_template, mood)
        return {'verb': {'infinitive': verb.infinitive, 
                         'template': verb.template,
                         'translation_en': verb.translation_en,
                         'stem': verb_stem}, 
                'moods': moods}

    def get_full_conjugation_for_mood(self, verb_stem, template, mood_name):
        ret = {}
        if mood_name not in template.moods:
            raise InvalidMoodError
        mood = template.moods[mood_name]

        for tense in mood.tenses:
            tense_template = mood.tenses[tense]
            ret[tense] = self._conjugate_specific_tense(verb_stem, mood_name, tense_template)
        return ret

    def _conjugate_specific_tense(self, verb_stem, mood_name, tense_template):
        ret = []
        if tense_template.name in TENSES_CONJUGATED_WITHOUT_PRONOUNS:
            for person in tense_template.persons:
                ret.append(verb_stem + person.get_ending())
        else:
            pronouns = grammar_defines.get_default_pronouns()
            for pronoun in pronouns:
                person = tense_template.get_person_ending_by_pronoun(pronoun)
                ending = person.get_ending()
                conjugation = self._conjugate_specific_tense_pronoun(verb_stem, ending, pronoun)
                if mood_name == 'subjunctive':
                    conjugation = prepend_with_que(conjugation)
                ret.append(conjugation)
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
