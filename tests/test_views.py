# -*- coding: utf-8 -*-

import pytest
from verbecc_svc import app 
from starlette.testclient import TestClient

client = TestClient(app)

expected_resp_etre = {"value":{
                "infinitive":"être",
                "infinitive_no_accents": "etre",
                "predicted": False,
                "pred_score": 1.0,
                "template":":être",
                "translation_en":"be",
                "impersonal": False}}
expected_resp_manger = {"value":{
                "infinitive":"manger",
                "infinitive_no_accents": "manger",
                "predicted": False,
                "pred_score": 1.0,
                "template":"man:ger",
                "translation_en":"eat",
                "impersonal": False}}
test_find_infinitive_data = [
    (u"manger", 200, expected_resp_manger),
    (u"être", 200, expected_resp_etre),
    (u"etre", 200, expected_resp_etre),
    (u"Être", 200, expected_resp_etre),
    (u"Etre", 200, expected_resp_etre)
]

expected_resp_conj_indicative_pouvoir = {
    "value": {
        "présent": [
            "je peux",
            "tu peux",
            "il peut",
            "nous pouvons",
            "vous pouvez",
            "ils peuvent"
        ],
        "imparfait": [
            "je pouvais",
            "tu pouvais",
            "il pouvait",
            "nous pouvions",
            "vous pouviez",
            "ils pouvaient"
        ],
        "futur-simple": [
            "je pourrai",
            "tu pourras",
            "il pourra",
            "nous pourrons",
            "vous pourrez",
            "ils pourront"
        ],
        "passé-simple": [
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
        ],
        "plus-que-parfait": [
            "j'avais pu",
            "tu avais pu",
            "il avait pu",
            "nous avions pu",
            "vous aviez pu",
            "ils avaient pu"
        ],
        "futur-antérieur": [
            "j'aurai pu",
            "tu auras pu",
            "il aura pu",
            "nous aurons pu",
            "vous aurez pu",
            "ils auront pu"
        ],
        "passé-antérieur": [
            "j'eus pu",
            "tu eus pu",
            "il eut pu",
            "nous eûmes pu",
            "vous eûtes pu",
            "ils eurent pu"
        ]
    }
}

test_conj_mood_data = [
    ("indicatif", "pouvoir", 200, expected_resp_conj_indicative_pouvoir),
    ("indicatif", "Pouvoir", 200, expected_resp_conj_indicative_pouvoir),
    ("indicatif", "oops", 404, {"detail": "Conjugator error"}),
    ("oops", "pouvoir", 404, {"detail": "Invalid mood"})
]

expected_resp_conj_manger = {
    "value": {
        "verb": {
            "infinitive": "manger",
            "predicted": False,
            "pred_score": 1.0,
            "template": "man:ger",
            "translation_en": "eat",
            "stem": "man"
        },
        "moods": {
            "infinitif": {
                "infinitif-présent": [
                    "manger"
                ]
            },
            "indicatif": {
                "présent": [
                    "je mange",
                    "tu manges",
                    "il mange",
                    "nous mangeons",
                    "vous mangez",
                    "ils mangent"
                ],
                "imparfait": [
                    "je mangeais",
                    "tu mangeais",
                    "il mangeait",
                    "nous mangions",
                    "vous mangiez",
                    "ils mangeaient"
                ],
                "futur-simple": [
                    "je mangerai",
                    "tu mangeras",
                    "il mangera",
                    "nous mangerons",
                    "vous mangerez",
                    "ils mangeront"
                ],
                "passé-simple": [
                    "je mangeai",
                    "tu mangeas",
                    "il mangea",
                    "nous mangeâmes",
                    "vous mangeâtes",
                    "ils mangèrent"
                ],
                "passé-composé": [
                    "j'ai mangé",
                    "tu as mangé",
                    "il a mangé",
                    "nous avons mangé",
                    "vous avez mangé",
                    "ils ont mangé"
                ],
                "plus-que-parfait": [
                    "j'avais mangé",
                    "tu avais mangé",
                    "il avait mangé",
                    "nous avions mangé",
                    "vous aviez mangé",
                    "ils avaient mangé"
                ],
                "futur-antérieur": [
                    "j'aurai mangé",
                    "tu auras mangé",
                    "il aura mangé",
                    "nous aurons mangé",
                    "vous aurez mangé",
                    "ils auront mangé"
                ],
                "passé-antérieur": [
                    "j'eus mangé",
                    "tu eus mangé",
                    "il eut mangé",
                    "nous eûmes mangé",
                    "vous eûtes mangé",
                    "ils eurent mangé"
                ]
            },
            "conditionnel": {
                "présent": [
                    "je mangerais",
                    "tu mangerais",
                    "il mangerait",
                    "nous mangerions",
                    "vous mangeriez",
                    "ils mangeraient"
                ],
                "passé": [
                    "j'aurais mangé",
                    "tu aurais mangé",
                    "il aurait mangé",
                    "nous aurions mangé",
                    "vous auriez mangé",
                    "ils auraient mangé"
                ]
            },
            "subjonctif": {
                "présent": [
                    "que je mange",
                    "que tu manges",
                    "qu'il mange",
                    "que nous mangions",
                    "que vous mangiez",
                    "qu'ils mangent"
                ],
                "imparfait": [
                    "que je mangeasse",
                    "que tu mangeasses",
                    "qu'il mangeât",
                    "que nous mangeassions",
                    "que vous mangeassiez",
                    "qu'ils mangeassent"
                ],
                "passé": [
                    "que j'aie mangé",
                    "que tu aies mangé",
                    "qu'il ait mangé",
                    "que nous ayons mangé",
                    "que vous ayez mangé",
                    "qu'ils aient mangé"
                ],
                "plus-que-parfait": [
                    "que j'eusse mangé",
                    "que tu eusses mangé",
                    "qu'il eût mangé",
                    "que nous eussions mangé",
                    "que vous eussiez mangé",
                    "qu'ils eussent mangé"
                ]
            },
            "imperatif": {
                "imperatif-présent": [
                    "mange",
                    "mangeons",
                    "mangez"
                ],
                "imperatif-passé": [
                    "aie mangé",
                    "ayons mangé",
                    "ayez mangé"
                ]
            },
            "participe": {
                "participe-présent": [
                    "mangeant"
                ],
                "participe-passé": [
                    "mangé",
                    "mangés",
                    "mangée",
                    "mangées"
                ]
            }
        }
    }
}

expected_resp_conj_pouvoir = {
    "value": {
        "verb": {
            "infinitive": "pouvoir",
            "predicted": False,
            "pred_score": 1.0,
            "template": "p:ouvoir",
            "translation_en": "power",
            "stem": "p"
        },
        "moods": {
            "infinitif": {
                "infinitif-présent": [
                    "pouvoir"
                ]
            },
            "indicatif": {
                "présent": [
                    "je peux",
                    "tu peux",
                    "il peut",
                    "nous pouvons",
                    "vous pouvez",
                    "ils peuvent"
                ],
                "imparfait": [
                    "je pouvais",
                    "tu pouvais",
                    "il pouvait",
                    "nous pouvions",
                    "vous pouviez",
                    "ils pouvaient"
                ],
                "futur-simple": [
                    "je pourrai",
                    "tu pourras",
                    "il pourra",
                    "nous pourrons",
                    "vous pourrez",
                    "ils pourront"
                ],
                "passé-simple": [
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
                ],
                "plus-que-parfait": [
                    "j'avais pu",
                    "tu avais pu",
                    "il avait pu",
                    "nous avions pu",
                    "vous aviez pu",
                    "ils avaient pu"
                ],
                "futur-antérieur": [
                    "j'aurai pu",
                    "tu auras pu",
                    "il aura pu",
                    "nous aurons pu",
                    "vous aurez pu",
                    "ils auront pu"
                ],
                "passé-antérieur": [
                    "j'eus pu",
                    "tu eus pu",
                    "il eut pu",
                    "nous eûmes pu",
                    "vous eûtes pu",
                    "ils eurent pu"
                ]
            },
            "conditionnel": {
                "présent": [
                    "je pourrais",
                    "tu pourrais",
                    "il pourrait",
                    "nous pourrions",
                    "vous pourriez",
                    "ils pourraient"
                ],
                "passé": [
                    "j'aurais pu",
                    "tu aurais pu",
                    "il aurait pu",
                    "nous aurions pu",
                    "vous auriez pu",
                    "ils auraient pu"
                ]
            },
            "subjonctif": {
                "présent": [
                    "que je puisse",
                    "que tu puisses",
                    "qu'il puisse",
                    "que nous puissions",
                    "que vous puissiez",
                    "qu'ils puissent"
                ],
                "imparfait": [
                    "que je pusse",
                    "que tu pusses",
                    "qu'il pût",
                    "que nous pussions",
                    "que vous pussiez",
                    "qu'ils pussent"
                ],
                "passé": [
                    "que j'aie pu",
                    "que tu aies pu",
                    "qu'il ait pu",
                    "que nous ayons pu",
                    "que vous ayez pu",
                    "qu'ils aient pu"
                ],
                "plus-que-parfait": [
                    "que j'eusse pu",
                    "que tu eusses pu",
                    "qu'il eût pu",
                    "que nous eussions pu",
                    "que vous eussiez pu",
                    "qu'ils eussent pu"
                ]
            },
            "imperatif": {
                "imperatif-présent": [],
                "imperatif-passé": []
            },
            "participe": {
                "participe-présent": [
                    "pouvant"
                ],
                "participe-passé": [
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
            "predicted": False,
            "pred_score": 1.0,
            "template": "pl:euvoir",
            "translation_en": "rain",
            "stem": "pl"
        },
        "moods": {
            "infinitif": {
                "infinitif-présent": [
                    "pleuvoir"
                ]
            },
            "indicatif": {
                "présent": [
                    "il pleut",
                    "ils pleuvent"
                ],
                "imparfait": [
                    "il pleuvait",
                    "ils pleuvaient"
                ],
                "futur-simple": [
                    "il pleuvra",
                    "ils pleuvront"
                ],
                "passé-simple": [
                    "il plut",
                    "ils plurent"
                ],
                "passé-composé": [
                    "il a plu",
                    "ils ont plu"
                ],
                "plus-que-parfait": [
                    "il avait plu",
                    "ils avaient plu"
                ],
                "futur-antérieur": [
                    "il aura plu",
                    "ils auront plu"
                ],
                "passé-antérieur": [
                    "il eut plu",
                    "ils eurent plu"
                ]
            },
            "conditionnel": {
                "présent": [
                    "il pleuvrait",
                    "ils pleuvraient"
                ],
                "passé": [
                    "il aurait plu",
                    "ils auraient plu"
                ]
            },
            "subjonctif": {
                "présent": [
                    "qu'il pleuve",
                    "qu'ils pleuvent"
                ],
                "imparfait": [
                    "qu'il plût",
                    "qu'ils plussent"
                ],
                "passé": [
                    "qu'il ait plu",
                    "qu'ils aient plu"
                ],
                "plus-que-parfait": [
                    "qu'il eût plu",
                    "qu'ils eussent plu"
                ]
            },
            "imperatif": {
                "imperatif-présent": [],
                "imperatif-passé": []
            },
            "participe": {
                "participe-présent": [
                    "pleuvant"
                ],
                "participe-passé": [
                    "plu",
                    "plus",
                    "plue",
                    "plues"
                ]
            }
        }
    }
}

expected_resp_conj_se_lever = {
    "value": {
        "verb": {
            "infinitive": "lever",
            "predicted": False,
            "pred_score": 1.0,
            "template": "l:ever",
            "translation_en": "lift",
            "stem": "l"
        },
        "moods": {
            "infinitif": {
                "infinitif-présent": [
                    "se lever"
                ]
            },
            "indicatif": {
                "présent": [
                    "je me lève",
                    "tu te lèves",
                    "il se lève",
                    "nous nous levons",
                    "vous vous levez",
                    "ils se lèvent"
                ],
                "imparfait": [
                    "je me levais",
                    "tu te levais",
                    "il se levait",
                    "nous nous levions",
                    "vous vous leviez",
                    "ils se levaient"
                ],
                "futur-simple": [
                    "je me lèverai",
                    "tu te lèveras",
                    "il se lèvera",
                    "nous nous lèverons",
                    "vous vous lèverez",
                    "ils se lèveront"
                ],
                "passé-simple": [
                    "je me levai",
                    "tu te levas",
                    "il se leva",
                    "nous nous levâmes",
                    "vous vous levâtes",
                    "ils se levèrent"
                ],
                "passé-composé": [
                    "je me suis levé",
                    "tu t'es levé",
                    "il s'est levé",
                    "nous nous sommes levés",
                    "vous vous êtes levés",
                    "ils se sont levés"
                ],
                "plus-que-parfait": [
                    "je m'étais levé",
                    "tu t'étais levé",
                    "il s'était levé",
                    "nous nous étions levés",
                    "vous vous étiez levés",
                    "ils s'étaient levés"
                ],
                "futur-antérieur": [
                    "je me serai levé",
                    "tu te seras levé",
                    "il se sera levé",
                    "nous nous serons levés",
                    "vous vous serez levés",
                    "ils se seront levés"
                ],
                "passé-antérieur": [
                    "je me fus levé",
                    "tu te fus levé",
                    "il se fut levé",
                    "nous nous fûmes levés",
                    "vous vous fûtes levés",
                    "ils se furent levés"
                ]
            },
            "conditionnel": {
                "présent": [
                    "je me lèverais",
                    "tu te lèverais",
                    "il se lèverait",
                    "nous nous lèverions",
                    "vous vous lèveriez",
                    "ils se lèveraient"
                ],
                "passé": [
                    "je me serais levé",
                    "tu te serais levé",
                    "il se serait levé",
                    "nous nous serions levés",
                    "vous vous seriez levés",
                    "ils se seraient levés"
                ]
            },
            "subjonctif": {
                "présent": [
                    "que je me lève",
                    "que tu te lèves",
                    "qu'il se lève",
                    "que nous nous levions",
                    "que vous vous leviez",
                    "qu'ils se lèvent"
                ],
                "imparfait": [
                    "que je me levasse",
                    "que tu te levasses",
                    "qu'il se levât",
                    "que nous nous levassions",
                    "que vous vous levassiez",
                    "qu'ils se levassent"
                ],
                "passé": [
                    "que je me sois levé",
                    "que tu te sois levé",
                    "qu'il se soit levé",
                    "que nous nous soyons levés",
                    "que vous vous soyez levés",
                    "qu'ils se soient levés"
                ],
                "plus-que-parfait": [
                    "que je me fusse levé",
                    "que tu te fusses levé",
                    "qu'il se fût levé",
                    "que nous nous fussions levés",
                    "que vous vous fussiez levés",
                    "qu'ils se fussent levés"
                ]
            },
            "imperatif": {
                "imperatif-présent": [
                    "lève-toi",
                    "levons-nous",
                    "levez-vous"
                ],
                "imperatif-passé": []
            },
            "participe": {
                "participe-présent": [
                    "se levant"
                ],
                "participe-passé": [
                    "s'étant levé",
                    "s'étant levés",
                    "s'étant levée",
                    "s'étant levées"
                ]
            }
        }
    }
}

test_conj_data = [
    ("fr", "manger", 200, expected_resp_conj_manger),
    ("fr", "pouvoir", 200, expected_resp_conj_pouvoir),
    ("fr", "Pouvoir", 200, expected_resp_conj_pouvoir),
    ("fr", "pleuvoir", 200, expected_resp_conj_pleuvoir),
    ("fr", "Se lever", 200, expected_resp_conj_se_lever),
    ("fr", "oops", 404, {"detail": "Conjugator error"}),
    ("oops", "oops", 404, {"detail": "Invalid language"})
]

test_find_template_data = [
    ("oops:ie", 404, {"detail": "Template not found"})
]

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"value": "Hello 世界"}

def test_supported_langs():
  response = client.get("/supported-langs")
  langs = response.json()["value"]
  assert langs['fr'] == 'français'
  assert langs['es'] == 'español'

@pytest.mark.parametrize("infinitive,expected_status,expected_resp", 
                         test_find_infinitive_data)
def test_find_infinitive(infinitive, expected_status, expected_resp):
    response = client.get("/find/infinitive/fr/{}".format(infinitive))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

@pytest.mark.parametrize("template,expected_status,expected_resp", 
                         test_find_template_data)
def test_find_conjugation_template(template, expected_status, expected_resp):
    response = client.get("/find/template/fr/{}".format(template))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

test_search_infinitive_data = [
    ("lev", 200, {
        "value": [
            "lever",
            "léviger",
            "levretter"
        ]
    }),
    ("Se lev", 200, {
        "value": [
            "se lever",
            "se léviger",
            "se levretter"
        ]
    }),
    ("s'aim", 200, {
        "value": [
            "s'aimanter",
            "s'aimer"
        ]
    })
]

@pytest.mark.parametrize("query,expected_status,expected_resp",
                         test_search_infinitive_data)
def test_search_infinitive(query, expected_status, expected_resp):
  response = client.get("/search/infinitive/fr/{}".format(query))
  assert response.status_code == expected_status
  assert set(response.json()["value"]) == set(expected_resp["value"])

@pytest.mark.parametrize("mood,infinitive,expected_status,expected_resp", 
                         test_conj_mood_data)
def test_conjugate_mood(mood, infinitive, 
                        expected_status, expected_resp):
    response = client.get(
        "/conjugate/fr/{}?mood={}".format(infinitive, mood))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

"""
def test_conjugate_mood_invalid_infinitive():
    response = client.get("/conjugate/fr/oops?mood=indicatif")
    assert response.status_code == 404
    assert response.json() == {"detail": "Verb not found"}
"""

def test_conjugate_mood_invalid_mood():
    response = client.get("/conjugate/fr/manger?mood=oops")
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid mood"}

def test_conjugate_mood_invalid_tense():
    response = client.get("/conjugate/fr/manger?mood=imperatif&tense=oops")
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid tense"}

@pytest.mark.parametrize("lang,infinitive,expected_status,expected_resp", 
                         test_conj_data)
def test_conjugate(lang, infinitive, 
                   expected_status, expected_resp):
    response = client.get(
        "/conjugate/{}/{}".format(lang, infinitive))
    assert response.status_code == expected_status
    assert response.json() == expected_resp

def test_conjugate_mood_tense():
    response = client.get(
    "/conjugate/fr/manger?mood=indicatif&tense=passé-composé")
    assert response.json() == {
        "value": [
            "j'ai mangé",
            "tu as mangé",
            "il a mangé",
            "nous avons mangé",
            "vous avez mangé",
            "ils ont mangé"
        ]
    }
