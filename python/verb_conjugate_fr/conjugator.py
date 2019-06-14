# -*- coding: utf-8 -*-

from __future__ import print_function

from .conjugation_template import ConjugationTemplate
from .conjugations_parser import ConjugationsParser
from .grammar_defines import *
from .mood import Mood
from .person_ending import PersonEnding
from .string_utils import (
    prepend_with_que,
    starts_with_vowel)
from .tense_template import TenseTemplate
from .verb import Verb
from .verbs_parser import (
    VerbNotFoundError, VerbsParser
)

class ConjugatorError(Exception):
    pass

class InvalidMoodError(Exception):
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

    def _get_conj_obs(self, infinitive):
        verb = self.verb_parser.find_verb_by_infinitive(infinitive)
        template = self.conj_parser.find_template(verb.template)
        verb_stem = get_verb_stem(verb.infinitive, template.name)
        return (verb, template, verb_stem)        

    def conjugate(self, infinitive):
        verb, template, verb_stem = self._get_conj_obs(infinitive)
        moods = {}
        for mood in template.moods:
            moods[mood] = self._get_full_conjugation_for_mood(
            verb, verb_stem, template, mood)
        return {'verb': {'infinitive': verb.infinitive, 
                         'template': verb.template,
                         'translation_en': verb.translation_en,
                         'stem': verb_stem}, 
                'moods': moods}

    def get_full_conjugation_for_mood(self, infinitive, mood_name):
        verb, template, verb_stem = self._get_conj_obs(infinitive)
        return self._get_full_conjugation_for_mood(verb, verb_stem, template, mood_name)

    def _get_full_conjugation_for_mood(self, verb, verb_stem, template, mood_name):
        ret = {}
        if mood_name not in template.moods:
            raise InvalidMoodError
        mood = template.moods[mood_name]

        for tense in mood.tenses:
            tense_template = mood.tenses[tense]
            ret[tense] = self._conjugate_specific_tense(verb_stem, mood_name, tense_template)

        if mood_name == 'indicative':
            ret['passé-composé'] = self._conjugate_passe_compose(verb, verb_stem, template)

        return ret

    def conjugate_passe_compose(self, infinitive):
        verb, template, verb_stem = self._get_conj_obs(infinitive)
        return self._conjugate_passe_compose(verb, verb_stem, template)

    def _conjugate_passe_compose(self, verb, verb_stem, template):
        helping_verb = 'avoir'
        if verb.infinitive in VERBS_CONJUGATED_WITH_ETRE_IN_PASSE_COMPOSE:
            helping_verb = 'être'
        hv_verb, hv_template, hv_verb_stem = self._get_conj_obs(helping_verb)
        hv_conj = self._conjugate_specific_tense(
            hv_verb_stem, 
            'indicative', 
            hv_template.moods['indicative'].tenses['present'])
        participle = self._conjugate_specific_tense(
            verb_stem, 
            'participle', 
            template.moods['participle'].tenses['past-participle'])
        ret = []
        if helping_verb == 'avoir':
            ret = [i + ' ' + participle[0] for i in hv_conj]
        else:
            ret = [i + ' ' + 
                participle[get_participle_inflection_from_pronoun(i).value] 
                for i in hv_conj]
        return ret

    def _conjugate_specific_tense(self, verb_stem, mood_name, tense_template):
        ret = []
        if tense_template.name in TENSES_CONJUGATED_WITHOUT_PRONOUNS:
            for person in tense_template.persons:
                ret.append(verb_stem + person.get_ending())
        else:
            pronouns = get_default_pronouns()
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
