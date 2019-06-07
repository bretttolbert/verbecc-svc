from verb_conjugate_fr import app 
from starlette.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"value": "Hello 世界"}

def test_read_conjugation():
    response = client.get("/conjugate/manger")
    assert response.status_code == 200

def test_read_conjugation_not_found():
    response = client.get("/conjugate/oops")
    assert response.status_code == 404
    assert response.json() == {"detail": "Verb not found"}

def test_read_find_infinitive():
    response = client.get("/find/infinitive/manger")
    assert response.status_code == 200
    assert response.json() == {"value":{
                            "infinitive":"manger",
                            "template":"man:ger",
                            "translation_en":"eat"}}

def test_read_find_infinitive_not_found():
    response = client.get("/find/infinitive/oops")
    assert response.status_code == 404
    assert response.json() == {"detail": "Verb not found"}

def test_read_find_conjugation_template():
    response = client.get("/find/conjugation-template/man:ger")
    assert response.status_code == 200

def test_read_find_conjugation_template_not_found():
    response = client.get("/find/conjugation-template/oops:ie")
    assert response.status_code == 404
    assert response.json() == {"detail": "Template not found"}

def test_read_conjugation_for_mood():
    response = client.get("/conjugate/mood/indicative/manger")
    assert response.status_code == 200

def test_read_conjugation_for_mood_invalid_mood():
    response = client.get("/conjugate/mood/oops/manger")
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid mood"}

def test_read_conjugation_for_mood_invalid_infinitive():
    response = client.get("/conjugate/mood/indicative/oops")
    assert response.status_code == 404
    assert response.json() == {"detail": "Verb not found"}
