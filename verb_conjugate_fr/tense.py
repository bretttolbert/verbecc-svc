# -*- coding: utf-8 -*-

from .person_ending import PersonEnding


class Tense:
    """
    Contains PersonEndings for a specific verb template, mood and tense
    Note: The template name and mood isn't specified because a Tense belongs to a Mood object
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
        """
        self.persons = []
        for p_elem in tense_elem.findall('p'):
            self.persons.append(PersonEnding(p_elem))

    def find_person_by_pronoun(self, pronoun):
        pronoun = pronoun.lower()
        if self.name in ('present', 'imperfect', 'future', 'simple-past'):
            if pronoun == 'je':
                return self.persons[0]
            elif pronoun == 'tu':
                return self.persons[1]
            elif pronoun in ('il', 'elle', 'on'):
                return self.persons[2]
            elif pronoun == 'nous':
                return self.persons[3]
            elif pronoun == 'vous':
                return self.persons[4]
            elif pronoun in ('ils', 'elles'):
                return self.persons[5]
        raise ValueError
