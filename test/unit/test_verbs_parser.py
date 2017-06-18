from mock import patch

import pytest

from verb_conjugate_fr.verbs_parser import (
    Verb, VerbsParser, VerbsParserError
)


def test_verbs_parser():
    vp = VerbsParser()
    assert len(vp.verbs) >= 7000


def test_verb():
    vp = VerbsParser()
    verb = vp.find_verb_by_infinitive("manger")
    assert verb.infinitive == "manger"
    assert verb.template == "man:ger"
    assert verb.translation_en == "eat"


def test_verb_not_found():
    vp = VerbsParser()
    with pytest.raises(ValueError):
        verb = vp.find_verb_by_infinitive("foo")


@patch('lxml.etree._Element')
def test_verb_invalid_xml(mock_v_elem):
    mock_v_elem.tag.return_value = "not-v"
    with pytest.raises(VerbsParserError):
        v = Verb(mock_v_elem)
