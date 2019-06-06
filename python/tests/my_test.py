from verb_conjugate_fr.run import get_hello

def test_get_hello():
	assert get_hello() == 'hello world'
