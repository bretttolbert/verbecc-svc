from verb_conjugate_fr import grammar_defines


def test_get_default_pronouns():
    assert grammar_defines.get_default_pronouns() == ['je', 'tu', 'il', 'nous', 'vous', 'ils']
