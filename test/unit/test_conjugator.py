# -*- coding: utf-8 -*-

from lxml import etree

from verb_conjugate_fr.conjugator import (
    Conjugator,
    conjugate_specific_mood_tense,
    get_verb_stem
)
from verb_conjugate_fr.tense import Tense


def test_conjugator():
    conj = Conjugator()
    conj.conjugate(u"manger")
    conj.conjugate(u"éparpiller")


def test_conjugator_conjugate_specific_mood_tense():
    verb_stem = u"man"
    parser = etree.XMLParser(encoding='utf-8')
    tense_elem = etree.fromstring(
        u"""<present>
        <p><i>ge</i></p>
        <p><i>ges</i></p>
        <p><i>ge</i></p>
        <p><i>geons</i></p>
        <p><i>gez</i></p>
        <p><i>gent</i></p>
        </present>""".encode('utf-8'),
        parser)
    tense_name = 'present'
    tense = Tense(tense_name, tense_elem)
    out = conjugate_specific_mood_tense(verb_stem, tense)
    assert out == u"present\nje mange\ntu manges\nil mange\n" + \
                  "nous mangeons\nvous mangez\nils mangent\n\n"


def test_conjugator_get_verb_stem():
    verb_stem = get_verb_stem("manger", "man:ger")
    assert verb_stem == "man"
    verb_stem = get_verb_stem("vendre", "ten:dre")
    assert verb_stem == "ven"
    verb_stem = get_verb_stem("aller", ":aller")
    assert verb_stem == ""
