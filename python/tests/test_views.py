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
