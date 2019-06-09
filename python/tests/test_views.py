# -*- coding: utf-8 -*-

import pytest
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

test_data = [
    (u"manger", 200, {"value":{
                "infinitive":"manger",
                "infinitive_no_accents": "manger",
                "template":"man:ger",
                "translation_en":"eat"}}),
    (u"être", 200, {"value":{
                "infinitive":"être",
                "infinitive_no_accents": "etre",
                "template":":être",
                "translation_en":"be"}}),
    (u"etre", 200, {"value":{
                "infinitive":"être",
                "infinitive_no_accents": "etre",
                "template":":être",
                "translation_en":"be"}}),
    (u"oops", 404, {"detail": "Verb not found"})
]

@pytest.mark.parametrize("infinitive,expected_status,expected_resp", test_data)
def test_read_find_infinitive(infinitive, expected_status, expected_resp):
    response = client.get("/find/infinitive/{}".format(infinitive))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

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
