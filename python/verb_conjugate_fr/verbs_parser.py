# -*- coding: utf-8 -*-

from __future__ import print_function

from bisect import bisect_left

from lxml import etree

from pkg_resources import resource_filename

from .string_utils import strip_accents
from .verb import (Verb, VerbsParserError)


class VerbNotFoundError(Exception):
    pass


class VerbsParser:
    def __init__(self):
        self.verbs = []
        parser = etree.XMLParser(encoding='utf-8')
        tree = etree.parse(resource_filename(
                           "verb_conjugate_fr",
                           "data/verbs_fr.xml"),
                           parser)
        root = tree.getroot()
        if root.tag != 'verbs-fr':
            raise VerbsParserError(
                "Root XML Tag <verbs-fr> Not Found")
        for child in root:
            if child.tag == 'v':
                self.verbs.append(Verb(child))
        self.verbs = sorted(self.verbs, key=lambda x: x.infinitive)
        self._keys = [verb.infinitive for verb in self.verbs]
        print('Loaded {} verbs'.format(len(self.verbs)))

    def find_verb_by_infinitive(self, infinitive):
        """Assumes verbs are already sorted by infinitive"""
        i = bisect_left(self._keys, infinitive)
        if i != len(self._keys) and self._keys[i] == infinitive:
            return self.verbs[i]
        raise VerbNotFoundError

    def get_verbs_that_start_with(self, pre):
        ret = []
        pre_no_accents = strip_accents(pre)
        for verb in self.verbs:
            infinitive_no_accents = strip_accents(verb.infinitive)
            if infinitive_no_accents.startswith(pre_no_accents):
                ret.append(verb)
        return ret


if __name__ == "__main__":
    vp = VerbsParser()
