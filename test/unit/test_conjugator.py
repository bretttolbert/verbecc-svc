# -*- coding: utf-8 -*-

from lxml import etree

from mock import patch

from verb_conjugate_fr.conjugator import (
    Conjugator,
    conjugate_specific_tense,
    conjugate_specific_tense_pronoun,
    get_verb_stem
)
from verb_conjugate_fr.tense import Tense


def test_conjugator_get_full_conjugation_string():
    conj = Conjugator()
    out = conj.get_full_conjugation_string(u"manger")
    assert len(out)
    assert u"je mange\n" in out
    out = conj.get_full_conjugation_string(u"éparpiller")
    assert len(out)
    assert u"j'éparpille\n" in out


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
    tense = Tense(tense_name, tense_elem)
    out = conjugate_specific_tense(verb_stem, tense)
    assert out == u"present\nje mange\ntu manges\nil mange\n" + \
                  u"nous mangeons\nvous mangez\nils mangent\n\n"


@patch('verb_conjugate_fr.person_ending.PersonEnding')
def test_conjugator_conjugate_specific_tense_pronoun(mock_person):
    verb_stem = u"man"
    pronoun = u"je"
    ending = u"ge"
    conjugation = conjugate_specific_tense_pronoun(verb_stem, ending, pronoun)
    assert conjugation == u"je mange"


def test_conjugator_get_verb_stem():
    verb_stem = get_verb_stem(u"manger", u"man:ger")
    assert verb_stem == u"man"
    verb_stem = get_verb_stem(u"vendre", u"ten:dre")
    assert verb_stem == u"ven"
    verb_stem = get_verb_stem(u"aller", u":aller")
    assert verb_stem == u""
