# -*- coding: utf-8 -*-


class PersonEnding:
    """
    aka <p>
    Ending for a specific verb template, mood, tense and grammatical person
    May also have an alternate ending for an alternative spelling.
    E.g. Ending for aim:er Indicative Present 2nd Person Plural = ['ez']
    E.g. Ending for pa:yer Indicative Present 1st Person Singular = ['ie', 'ye']
    Explanation: 'ye' is an alternate spelling (je paie, je paye)
    p_elem
        Example p_elem:
            <p><i>eoir</i><i>oir</i></p>

    default_p_elem
        This will be used in place of p_elem if p_elem contains no <i> elements.
        See comment in tense_template.__init__ for explanation.
    """
    def __init__(self, p_elem, default_p_elem):
        self._endings = []
        i_elems = p_elem.findall('i')
        if len(i_elems) == 0:
            i_elems = default_p_elem.findall('i')
        for i_elem in i_elems:
            ending = u''
            if i_elem.text is not None:
                ending += i_elem.text
            self._endings.append(ending)

    def get_ending(self):
        return self._endings[0]

    def get_alternate_ending(self):
        ret = None
        if len(self._endings) > 1:
            ret = self._endings[1]
        return ret
