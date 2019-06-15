# -*- coding: utf-8 -*-

from __future__ import print_function

from .conjugation_template import ConjugationTemplate
from .conjugations_parser import ConjugationsParser
from .grammar_defines import *
from .mood import Mood
from .person_ending import PersonEnding
from .string_utils import (
    prepend_with_que,
    prepend_with_se,
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
        self._tag_impersonal_verbs()

    def _tag_impersonal_verbs(self):
        self.impersonal_verbs = []
        for verb in self.verb_parser.verbs:
            if verb.template in self.conj_parser.impersonal_templates:
                verb.impersonal = True
                self.impersonal_verbs.append(verb.infinitive)

    def verb_can_be_reflexive(self, infinitive):
        return (infinitive not in self.impersonal_verbs 
            and infinitive not in 
            VERBS_THAT_CANNOT_BE_REFLEXIVE_OTHER_THAN_IMPERSONAL_VERBS) 

    class ConjugationObjects:
        def __init__(self, infinitive, verb, template, verb_stem, is_reflexive):
            self.infinitive = infinitive
            self.verb = verb
            self.template = template
            self.verb_stem = verb_stem
            self.is_reflexive = is_reflexive

    def _get_conj_obs(self, infinitive):
        is_reflexive = False
        if infinitive.startswith("se "):
            is_reflexive = True
            infinitive = infinitive[3:]
        elif infinitive.startswith("s'"):
            is_reflexive = True
            infinitive = infinitive[2:]
        if is_reflexive and not self.verb_can_be_reflexive(infinitive):
            raise VerbNotFoundError("Verb cannot be reflexive")
        verb = self.verb_parser.find_verb_by_infinitive(infinitive)
        template = self.conj_parser.find_template(verb.template)
        verb_stem = get_verb_stem(verb.infinitive, template.name)
        return Conjugator.ConjugationObjects(
            infinitive, verb, template, verb_stem, is_reflexive)      

    def conjugate(self, infinitive):
        co = self._get_conj_obs(infinitive)
        moods = {}
        for mood in co.template.moods:
            moods[mood] = self._get_full_conjugation_for_mood(co, mood)
        return {'verb': {'infinitive': co.verb.infinitive, 
                         'template': co.verb.template,
                         'translation_en': co.verb.translation_en,
                         'stem': co.verb_stem}, 
                'moods': moods}

    def get_full_conjugation_for_mood(self, infinitive, mood_name):
        co = self._get_conj_obs(infinitive)
        return self._get_full_conjugation_for_mood(co, mood_name)

    def _get_full_conjugation_for_mood(self, co, mood_name):
        ret = {}
        if mood_name not in co.template.moods:
            raise InvalidMoodError
        mood = co.template.moods[mood_name]

        for tense in mood.tenses:
            tense_template = mood.tenses[tense]
            ret[tense] = self._conjugate_specific_tense(
                co.verb_stem, mood_name, tense_template,
                co.is_reflexive)

        if mood_name == 'indicative':
            ret['passé-composé'] = self._conjugate_passe_compose(co)

        return ret

    def conjugate_passe_compose(self, infinitive):
        co = self._get_conj_obs(infinitive)
        return self._conjugate_passe_compose(co)

    def _conjugate_passe_compose(self, co):
        helping_verb = 'avoir'
        if (co.verb.infinitive in VERBS_CONJUGATED_WITH_ETRE_IN_PASSE_COMPOSE
            or co.is_reflexive):
            helping_verb = 'être'
        hvco = self._get_conj_obs(helping_verb)
        hvconj = self._conjugate_specific_tense(
            hvco.verb_stem, 
            'indicative', 
            hvco.template.moods['indicative'].tenses['present'],
            co.is_reflexive)
        participle = self._conjugate_specific_tense(
            co.verb_stem, 
            'participle', 
            co.template.moods['participle'].tenses['past-participle'])
        ret = []
        if helping_verb == 'avoir':
            ret = [i + ' ' + participle[0] for i in hvconj]
        else:
            ret = [i + ' ' + 
                participle[get_participle_inflection_by_pronoun(i).value] 
                for i in hvconj]
        return ret

    def _conjugate_specific_tense(self, verb_stem, mood_name, 
                                  tense_template, is_reflexive=False):
        ret = []
        if tense_template.name in TENSES_CONJUGATED_WITHOUT_PRONOUNS:
            for person_ending in tense_template.person_endings:
                conj = ''
                if is_reflexive and tense_template.name == 'past-participle':
                    conj += 'étant '
                conj += verb_stem + person_ending.get_ending()
                if is_reflexive:
                    if mood_name != 'imperative':
                        conj = prepend_with_se(conj)
                    else:
                        conj += get_pronoun_suffix(person_ending.get_person())
                ret.append(conj)
        else:
            for person_ending in tense_template.person_endings:
                pronoun = get_default_pronoun(
                    person_ending.get_person(), is_reflexive)
                ending = person_ending.get_ending()
                conjugation = self._conjugate_specific_tense_pronoun(
                    verb_stem, ending, pronoun)
                if mood_name == 'subjunctive':
                    conjugation = prepend_with_que(conjugation)
                ret.append(conjugation)
        return ret

    def _conjugate_specific_tense_pronoun(self, verb_stem, ending, pronoun):
        ret = u''
        conjugated_verb = verb_stem + ending
        if pronoun[-1] == "e" and starts_with_vowel(conjugated_verb):
            ret += pronoun[:-1] + "'"
        else:
            ret += pronoun + " "
        ret += conjugated_verb
        return ret
