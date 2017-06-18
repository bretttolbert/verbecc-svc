from mock import patch

import pytest

from verb_conjugate_fr.conjugator import Conjugator


def test_conjugator():
    conj = Conjugator()
    conj.conjugate_verb("manger")
