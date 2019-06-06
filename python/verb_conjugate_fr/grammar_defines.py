from enum import Enum


class Person(Enum):
    FirstPersonSingular = 1
    SecondPersonSingular = 2
    ThirdPersonSingular = 3
    FirstPersonPlural = 4
    SecondPersonPlural = 5
    ThirdPersonPlural = 6


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
