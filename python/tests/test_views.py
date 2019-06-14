# -*- coding: utf-8 -*-

import pytest
from verb_conjugate_fr import app 
from starlette.testclient import TestClient

client = TestClient(app)

expected_resp_etre = {"value":{
                "infinitive":"être",
                "infinitive_no_accents": "etre",
                "template":":être",
                "translation_en":"be"}}
expected_resp_manger = {"value":{
                "infinitive":"manger",
                "infinitive_no_accents": "manger",
                "template":"man:ger",
                "translation_en":"eat"}}
test_find_infinitive_data = [
    (u"manger", 200, expected_resp_manger),
    (u"être", 200, expected_resp_etre),
    (u"etre", 200, expected_resp_etre),
    (u"Être", 200, expected_resp_etre),
    (u"Etre", 200, expected_resp_etre),
    (u"oops", 404, {"detail": "Verb not found"})
]

expected_resp_conj_indicative_pouvoir = {
  "value": {
    "present": [
      "je peux",
      "tu peux",
      "il peut",
      "nous pouvons",
      "vous pouvez",
      "ils peuvent"
    ],
    "imperfect": [
      "je pouvais",
      "tu pouvais",
      "il pouvait",
      "nous pouvions",
      "vous pouviez",
      "ils pouvaient"
    ],
    "future": [
      "je pourrai",
      "tu pourras",
      "il pourra",
      "nous pourrons",
      "vous pourrez",
      "ils pourront"
    ],
    "simple-past": [
      "je pus",
      "tu pus",
      "il put",
      "nous pûmes",
      "vous pûtes",
      "ils purent"
    ],
    "passé-composé": [
      "j'ai pu",
      "tu as pu",
      "il a pu",
      "nous avons pu",
      "vous avez pu",
      "ils ont pu"
    ]
  }
}

test_conj_mood_data = [
    ("indicative", "pouvoir", 200, expected_resp_conj_indicative_pouvoir),
    ("indicative", "Pouvoir", 200, expected_resp_conj_indicative_pouvoir),
    ("indicative", "oops", 404, {"detail": "Verb not found"}),
    ("oops", "pouvoir", 404, {"detail": "Invalid mood"})
]

expected_resp_conj_pouvoir = {
  "value": {
    "verb": {
      "infinitive": "pouvoir",
      "template": "p:ouvoir",
      "translation_en": "power",
      "stem": "p"
    },
    "moods": {
      "infinitive": {
        "infinitive-present": [
          "pouvoir"
        ]
      },
      "indicative": {
        "present": [
          "je peux",
          "tu peux",
          "il peut",
          "nous pouvons",
          "vous pouvez",
          "ils peuvent"
        ],
        "imperfect": [
          "je pouvais",
          "tu pouvais",
          "il pouvait",
          "nous pouvions",
          "vous pouviez",
          "ils pouvaient"
        ],
        "future": [
          "je pourrai",
          "tu pourras",
          "il pourra",
          "nous pourrons",
          "vous pourrez",
          "ils pourront"
        ],
        "simple-past": [
          "je pus",
          "tu pus",
          "il put",
          "nous pûmes",
          "vous pûtes",
          "ils purent"
        ],
        "passé-composé": [
          "j'ai pu",
          "tu as pu",
          "il a pu",
          "nous avons pu",
          "vous avez pu",
          "ils ont pu"
        ]
      },
      "conditional": {
        "present": [
          "je pourrais",
          "tu pourrais",
          "il pourrait",
          "nous pourrions",
          "vous pourriez",
          "ils pourraient"
        ]
      },
      "subjunctive": {
        "present": [
          "que je puisse",
          "que tu puisses",
          "qu'il puisse",
          "que nous puissions",
          "que vous puissiez",
          "qu'ils puissent"
        ],
        "imperfect": [
          "que je pusse",
          "que tu pusses",
          "qu'il pût",
          "que nous pussions",
          "que vous pussiez",
          "qu'ils pussent"
        ]
      },
      "imperative": {
        "imperative-present": []
      },
      "participle": {
        "present-participle": [
          "pouvant"
        ],
        "past-participle": [
          "pu",
          "pus",
          "pue",
          "pues"
        ]
      }
    }
  }
}

expected_resp_conj_pleuvoir = {
  "value": {
    "verb": {
      "infinitive": "pleuvoir",
      "template": "pl:euvoir",
      "translation_en": "rain",
      "stem": "pl"
    },
    "moods": {
      "infinitive": {
        "infinitive-present": [
          "pleuvoir"
        ]
      },
      "indicative": {
        "present": [
          "il pleut",
          "ils pleuvent"
        ],
        "imperfect": [
          "il pleuvait",
          "ils pleuvaient"
        ],
        "future": [
          "il pleuvra",
          "ils pleuvront"
        ],
        "simple-past": [
          "il plut"
        ],
        "passé-composé": [
          "j'ai plu",
          "tu as plu",
          "il a plu",
          "nous avons plu",
          "vous avez plu",
          "ils ont plu"
        ]
      },
      "conditional": {
        "present": [
          "il pleuvrait",
          "ils pleuvraient"
        ]
      },
      "subjunctive": {
        "present": [
          "qu'il pleuve",
          "qu'ils pleuvent"
        ],
        "imperfect": [
          "qu'il plût"
        ]
      },
      "imperative": {
        "imperative-present": []
      },
      "participle": {
        "present-participle": [
          "pleuvant"
        ],
        "past-participle": [
          "plu",
          "plus",
          "plue",
          "plues"
        ]
      }
    }
  }
}

test_conj_data = [
    ("pouvoir", 200, expected_resp_conj_pouvoir),
    ("Pouvoir", 200, expected_resp_conj_pouvoir),
    ("pleuvoir", 200, expected_resp_conj_pleuvoir),
    ("oops", 404, {"detail": "Verb not found"})
]

test_find_template_data = [
    ("oops:ie", 404, {"detail": "Template not found"})
]

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"value": "Hello 世界"}

@pytest.mark.parametrize("infinitive,expected_status,expected_resp", 
                         test_find_infinitive_data)
def test_read_find_infinitive(infinitive, expected_status, expected_resp):
    response = client.get("/find/infinitive/{}".format(infinitive))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

@pytest.mark.parametrize("template,expected_status,expected_resp", 
                         test_find_template_data)
def test_read_find_conjugation_template(template, expected_status, expected_resp):
    response = client.get("/find/conjugation-template/{}".format(template))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

@pytest.mark.parametrize("mood,infinitive,expected_status,expected_resp", 
                         test_conj_mood_data)
def test_read_conjugation_for_mood(mood, infinitive, 
                                   expected_status, expected_resp):
    response = client.get(
        "/conjugate/mood/{}/{}".format(mood, infinitive))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

def test_read_conjugation_for_mood_invalid_mood():
    response = client.get("/conjugate/mood/oops/manger")
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid mood"}

def test_read_conjugation_for_mood_invalid_infinitive():
    response = client.get("/conjugate/mood/indicative/oops")
    assert response.status_code == 404
    assert response.json() == {"detail": "Verb not found"}

@pytest.mark.parametrize("infinitive,expected_status,expected_resp", 
                         test_conj_data)
def test_read_conjugation(infinitive, 
                          expected_status, expected_resp):
    response = client.get(
        "/conjugate/{}".format(infinitive))
    assert response.status_code == expected_status
    assert response.json() == expected_resp
