# -*- coding: utf-8 -*-

import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def starts_with_vowel(s):
    if len(s) == 0:
        return False
    return strip_accents(s)[0] in ('a', 'e', 'i', 'o', 'u')

def prepend_with_que(pronoun_string):
    if starts_with_vowel(pronoun_string):
        return "qu'" + pronoun_string
    else:
        return "que " + pronoun_string

def unicodefix(s):
    # Fix Python 2.x.
    try:
        return s.decode('utf-8')
    except AttributeError:
        return s
