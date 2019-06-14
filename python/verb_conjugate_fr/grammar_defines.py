from enum import Enum

class Person(Enum):
    FirstPersonSingular = 0
    SecondPersonSingular = 1
    ThirdPersonSingular = 2
    FirstPersonPlural = 3
    SecondPersonPlural = 4
    ThirdPersonPlural = 5

class ParticipleInflection(Enum):
    MasculineSingular = 0
    MasculinePlural = 1
    FeminineSingular = 2
    FemininePlural = 3

TENSES_CONJUGATED_WITHOUT_PRONOUNS = ['infinitive-present', 'present-participle', 
                                      'imperative-present', 'past-participle']
VERBS_CONJUGATED_WITH_ETRE_IN_PASSE_COMPOSE = [
"aller",
"arriver",
"descendre",
"redescendre",
"entrer",
"rentrer",
"monter",
"remonter",
"mourir",
"naître",
"renaître",
"partir",
"repartir",
"passer",
"rester",
"retourner",
"sortir",
"ressortir",
"tomber",
"retomber",
"venir",
"devenir",
"parvenir",
"revenir"]

def get_default_pronoun(person):
    if person == Person.FirstPersonSingular:
        return 'je'
    elif person == Person.SecondPersonSingular:
        return 'tu'
    elif person == Person.ThirdPersonSingular:
        return 'il'
    elif person == Person.FirstPersonPlural:
        return 'nous'
    elif person == Person.SecondPersonPlural:
        return 'vous'
    elif person == Person.ThirdPersonPlural:
        return 'ils'
    return None

def get_default_pronouns():
    return list(map(get_default_pronoun, Person))
        
def get_participle_inflection_from_pronoun(conjugation):
    if conjugation.startswith('j'):
        return ParticipleInflection.MasculineSingular
    elif conjugation.startswith('tu'):
        return ParticipleInflection.MasculineSingular
    elif conjugation.startswith('ils'):
        return ParticipleInflection.MasculinePlural
    elif conjugation.startswith('elles'):
        return ParticipleInflection.FemininePlural
    elif conjugation.startswith('il'):
        return ParticipleInflection.MasculineSingular
    elif conjugation.startswith('on'):
        return ParticipleInflection.MasculineSingular
    elif conjugation.startswith('elle'):
        return ParticipleInflection.FeminineSingular
    elif conjugation.startswith('nous'):
        return ParticipleInflection.MasculinePlural
    elif conjugation.startswith('vous'):
        return ParticipleInflection.MasculinePlural
    raise ValueError
