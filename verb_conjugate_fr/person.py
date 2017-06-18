import codecs
from enum import Enum


class Person:
    """
    aka <p>
    Ending(s) for a specific conjugation template, mood, tense and grammatical person
    E.g. Ending(s) for aim:er Indicative Present 2nd Person Plural = ['ez']
    E.g. Endings(s) for pa:yer Indicative Present 1st Person Singular = ['ie', 'ye']
    Explanation: 'ye' is an alternate spelling (je paie, je paye)
    p_elem
        Example p_elem:
            <p><i>eoir</i><i>oir</i></p>
    """
    def __init__(self, p_elem):
        self.endings = []
        for i_elem in p_elem.findall('i'):
            ending = i_elem.text
            if ending is None:
                ending = ''
            self.endings.append(ending)

    def get_ending(self):
        return self.endings[0]

    def get_alternate_ending(self):
        ret = None
        if len(self.endings) > 1:
            ret = self.endings[1]
        return ret
