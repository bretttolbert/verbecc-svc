from lxml import etree

from .mood import (MOOD_TENSES, Mood)


class TemplateError(Exception):
    pass


class Template:
    def __init__(self, template_elem):
        if template_elem.tag != 'template':
            raise TemplateError("not a 'template' elem")
        try:
            self.name = template_elem.get('name')
            self.moods = {}
            for mood_name, mood_tenses in MOOD_TENSES.items():
                self.moods[mood_name] = \
                    Mood(mood_name, template_elem.find(mood_name))

        except AttributeError as e:
            raise TemplateError(
                "Error parsing {}: {}".format(
                    etree.tostring(template_elem),
                    str(e)))
