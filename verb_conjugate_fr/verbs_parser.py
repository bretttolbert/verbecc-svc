from __future__ import print_function

from bisect import bisect_left

from lxml import etree

from pkg_resources import resource_filename

from .verb import (Verb, VerbsParserError)


class VerbNotFoundError(Exception):
    pass


class VerbsParser:
    def __init__(self):
        self.verbs = []
        tree = etree.parse(resource_filename("verb_conjugate_fr", "data/verbs_fr.xml"))
        print(tree)
        root = tree.getroot()
        print(root)
        if root.tag != 'verbs-fr':
            raise VerbsParserError(
                "Root XML Tag <verbs-fr> Not Found")
        for child in root:
            if child.tag == 'v':
                self.verbs.append(Verb(child))
        self.verbs = sorted(self.verbs, key=lambda x: x.infinitive)
        self._keys = [verb.infinitive for verb in self.verbs]
        print('loaded {} verbs'.format(len(self.verbs)))

    def find_verb_by_infinitive(self, infinitive):
        """Assumes verbs are already sorted by infinitive"""
        i = bisect_left(self._keys, infinitive)
        if i != len(self._keys) and self._keys[i] == infinitive:
            return self.verbs[i]
        raise VerbNotFoundError


if __name__ == "__main__":
    vp = VerbsParser()
