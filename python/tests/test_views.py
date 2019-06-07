from verb_conjugate_fr import app 
from starlette.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"value": "Hello 世界"}

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
