# -*- coding: utf-8 -*-

import pytest
from lxml import etree
from mock import patch
from verb_conjugate_fr.conjugator import (
    Conjugator,
    ConjugatorError,
    get_verb_stem,
    prepend_with_que
)
from verb_conjugate_fr.tense_template import TenseTemplate

conj = Conjugator()

test_verbs = [
    (u"manger"), 
    (u"venir"), 
    (u"être"), 
    (u"aller"), 
    (u"pouvoir"), 
    (u"finir")
]

@pytest.mark.parametrize("infinitive", test_verbs)
def test_conjugator_conjugate(infinitive):
    for infinitive in test_verbs:
        output = conj.conjugate(infinitive)
        assert output

def test_conjugator_conjugate_specific_tense():
    verb_stem = u"man"
    tense_elem = etree.fromstring(
        u"""<present>
        <p><i>ge</i></p>
        <p><i>ges</i></p>
        <p><i>ge</i></p>
        <p><i>geons</i></p>
        <p><i>gez</i></p>
        <p><i>gent</i></p>
        </present>""")
    tense_name = 'present'
    tense = TenseTemplate(tense_name, tense_elem)
    out = conj._conjugate_specific_tense(verb_stem, 'indicative', tense)
    assert len(out) == 6
    assert out == [u"je mange", u"tu manges", u"il mange", u"nous mangeons", u"vous mangez", u"ils mangent"]

def test_conjugator_conjugate_passe_compose_with_avoir():
    assert conj.conjugate_passe_compose('manger') == [
    "j'ai mangé",
    "tu as mangé",
    "il a mangé",
    "nous avons mangé",
    "vous avez mangé",
    "ils ont mangé"
    ]

def test_conjugator_conjugate_passe_compose_with_etre():
    assert conj.conjugate_passe_compose('aller') == [
    "je suis allé",
    "tu es allé",
    "il est allé",
    "nous sommes allés",
    "vous êtes allés",
    "ils sont allés"
    ]

@patch('verb_conjugate_fr.person_ending.PersonEnding')
def test_conjugator_conjugate_specific_tense_pronoun(mock_person):
    verb_stem = u"man"
    pronoun = u"je"
    ending = u"ge"
    conjugation = conj._conjugate_specific_tense_pronoun(verb_stem, ending, pronoun)
    assert conjugation == u"je mange"

def test_conjugator_prepend_with_que():
    assert prepend_with_que("tu manges") == "que tu manges"
    assert prepend_with_que("il mange") == "qu'il mange"
    assert prepend_with_que("elles mangent") == "qu'elles mangent"

def test_conjugator_get_verb_stem():
    verb_stem = get_verb_stem(u"manger", u"man:ger")
    assert verb_stem == u"man"
    verb_stem = get_verb_stem(u"téléphoner", u"aim:er")
    assert verb_stem == u"téléphon"
    verb_stem = get_verb_stem(u"vendre", u"ten:dre")
    assert verb_stem == u"ven"
    # In the case of irregular verbs, the verb stem is empty string
    verb_stem = get_verb_stem(u"aller", u":aller")
    assert verb_stem == u""
    # The infinitive ending must match the template ending
    with pytest.raises(ConjugatorError):
        verb_stem = get_verb_stem(u"vendre", u"man:ger")
