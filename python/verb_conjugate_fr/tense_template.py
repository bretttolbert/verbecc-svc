# -*- coding: utf-8 -*-

from .person_ending import PersonEnding
from .grammar_defines import Person, get_person_by_pronoun


class TenseTemplate:
    """
    Contains PersonEndings for a specific verb template, mood and tense
    Note: The template name and mood is only known by the Mood object
          which owns this Tense.
    Class relationships:
        ConjugationTemplate has many Mood
            Mood has many Tense
                Tense has many PersonEnding
    E.g. aim:er indicative present
    name
        the name of the tense, e.g. "present"
    tense_elem
        A tense_elem contains one or more <p> (PersonEnding) elems
        Example tense_elem children:
            <p><i>e</i></p>
            <p><i>es</i></p>
            <p><i>e</i></p>
            <p><i>ons</i></p>
            <p><i>ez</i></p>
            <p><i>ent</i></p>
    """
    def __init__(self, name, tense_elem):
        self.name = name
        """
        There are six persons corresponding to grammar_defines.Person
        [0]= 1st person singular (je)
        [1]= 2nd person singular (tu)
        [2]= 3rd person singular (il, elle, on)
        [3]= 1st person plural (nous)
        [4]= 2nd person plural (vous)
        [5]= 3rd person plural (ils, elles)

        The following tenses have all 6 Persons:
          present, imperfect, future, simple-past
        These do not:
          infinitive-present has only 1
          imperative-present has 3
          present-participle has 1
          past-participle has 4

        For some verbs, e.g. être, the past-participle
        is the same for all 4 variants, so the xml omits them:
            <p><i>été</i></p>
            <p></p>
            <p></p>
            <p></p>
        Workaround: We do not add a PersonEnding unless it contains an <i>

        Also some verbs are impersonal, e.g. pleuvoir, so they don't have
        ending for all pronouns. Just 3rd person singular and plural

            <p></p>
            <p></p>
            <p><i>eut</i></p>
            <p></p>
            <p></p>
            <p><i>euvent</i></p>
        """
        self.person_endings = []
        person_num = 0
        for p_elem in tense_elem.findall('p'):
            person_ending = PersonEnding(p_elem, Person(person_num))
            person_num += 1
            if len(person_ending.endings) > 0:
                self.person_endings.append(person_ending)

    def get_person_ending_by_pronoun(self, pronoun):
        if self.name in ('present', 'imperfect', 'future', 'simple-past'):
            return self.person_endings[get_person_by_pronoun(pronoun).value]
        raise ValueError
