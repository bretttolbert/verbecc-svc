# -*- coding: utf-8 -*-

from lxml import etree

from mock import patch

import pytest

from verb_conjugate_fr.conjugator import (
    Conjugator,
    ConjugatorError,
    get_verb_stem
)
from verb_conjugate_fr.tense_template import TenseTemplate

conj = Conjugator()


def test_conjugator_conjugate():
    output = conj.conjugate(u"manger")
    assert output == {
        'moods': {
            u'indicative': {
                u'present': [
                    u'je mange',
                    u'tu manges',
                    u'il mange',
                    u'nous mangeons',
                    u'vous mangez',
                    u'ils mangent'
                ], u'imperfect': [
                    u'je mangeais',
                    u'tu mangeais',
                    u'il mangeait',
                    u'nous mangions',
                    u'vous mangiez',
                    u'ils mangeaient'
                ], u'future': [
                    u'je mangerai',
                    u'tu mangeras',
                    u'il mangera',
                    u'nous mangerons',
                    u'vous mangerez',
                    u'ils mangeront'
                ], u'simple-past': [
                    u'je mangeai',
                    u'tu mangeas',
                    u'il mangea',
                    u'nous mangeâmes',
                    u'vous mangeâtes',
                    u'ils mangèrent'
                ]
            }
        }
    }


def test_conjugator_get_full_conjugation_string():
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
    tense = TenseTemplate(tense_name, tense_elem)
    out = conj._conjugate_specific_tense(verb_stem, tense)
    assert len(out) == 6
    assert out == [u"je mange", u"tu manges", u"il mange", u"nous mangeons", u"vous mangez", u"ils mangent"]


@patch('verb_conjugate_fr.person_ending.PersonEnding')
def test_conjugator_conjugate_specific_tense_pronoun(mock_person):
    verb_stem = u"man"
    pronoun = u"je"
    ending = u"ge"
    conjugation = conj._conjugate_specific_tense_pronoun(verb_stem, ending, pronoun)
    assert conjugation == u"je mange"


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
