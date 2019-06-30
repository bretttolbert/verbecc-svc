# -*- coding: utf-8 -*-

import pytest
from verb_conjugate_fr import app 
from starlette.testclient import TestClient

client = TestClient(app)

expected_resp_etre = {"value":{
                "infinitive":"être",
                "infinitive_no_accents": "etre",
                "template":":être",
                "translation_en":"be",
                "impersonal": False}}
expected_resp_manger = {"value":{
                "infinitive":"manger",
                "infinitive_no_accents": "manger",
                "template":"man:ger",
                "translation_en":"eat",
                "impersonal": False}}
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
    ],
    "pluperfect": [
      "j'avais pu",
      "tu avais pu",
      "il avait pu",
      "nous avions pu",
      "vous aviez pu",
      "ils avaient pu"
    ],
    "future-perfect": [
      "j'aurai pu",
      "tu auras pu",
      "il aura pu",
      "nous aurons pu",
      "vous aurez pu",
      "ils auront pu"
    ],
    "anterior-past": [
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
        ],
        "pluperfect": [
          "j'avais pu",
          "tu avais pu",
          "il avait pu",
          "nous avions pu",
          "vous aviez pu",
          "ils avaient pu"
        ],
        "future-perfect": [
          "j'aurai pu",
          "tu auras pu",
          "il aura pu",
          "nous aurons pu",
          "vous aurez pu",
          "ils auront pu"
        ],
        "anterior-past": [
          "j'eus pu",
          "tu eus pu",
          "il eut pu",
          "nous eûmes pu",
          "vous eûtes pu",
          "ils eurent pu"
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
        ],
        "past": [
          "j'aurais pu",
          "tu aurais pu",
          "il aurait pu",
          "nous aurions pu",
          "vous auriez pu",
          "ils auraient pu"
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
        ],
        "past": [
          "que j'aie pu",
          "que tu aies pu",
          "qu'il ait pu",
          "que nous ayons pu",
          "que vous ayez pu",
          "qu'ils aient pu"
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
          "il a plu",
          "ils ont plu"
        ],
        "pluperfect": [
          "il avait plu",
          "ils avaient plu"
        ],
        "future-perfect": [
          "il aura plu",
          "ils auront plu"
        ],
        "anterior-past": [
          "il eut plu",
          "ils eurent plu"
        ]
      },
      "conditional": {
        "present": [
          "il pleuvrait",
          "ils pleuvraient"
        ],
        "past": [
          "il aurait plu",
          "ils auraient plu"
        ]
      },
      "subjunctive": {
        "present": [
          "qu'il pleuve",
          "qu'ils pleuvent"
        ],
        "imperfect": [
          "qu'il plût"
        ],
        "past": [
          "qu'il ait plu",
          "qu'ils aient plu"
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

expected_resp_conj_se_lever = {
  "value": {
    "verb": {
      "infinitive": "lever",
      "template": "l:ever",
      "translation_en": "lift",
      "stem": "l"
    },
    "moods": {
      "infinitive": {
        "infinitive-present": [
          "se lever"
        ]
      },
      "indicative": {
        "present": [
          "je me lève",
          "tu te lèves",
          "il se lève",
          "nous nous levons",
          "vous vous levez",
          "ils se lèvent"
        ],
        "imperfect": [
          "je me levais",
          "tu te levais",
          "il se levait",
          "nous nous levions",
          "vous vous leviez",
          "ils se levaient"
        ],
        "future": [
          "je me lèverai",
          "tu te lèveras",
          "il se lèvera",
          "nous nous lèverons",
          "vous vous lèverez",
          "ils se lèveront"
        ],
        "simple-past": [
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
        "pluperfect": [
          "je m'étais levé",
          "tu t'étais levé",
          "il s'était levé",
          "nous nous étions levés",
          "vous vous étiez levés",
          "ils s'étaient levés"
        ],
        "future-perfect": [
          "je me serai levé",
          "tu te seras levé",
          "il se sera levé",
          "nous nous serons levés",
          "vous vous serez levés",
          "ils se seront levés"
        ],
        "anterior-past": [
          "je me fus levé",
          "tu te fus levé",
          "il se fut levé",
          "nous nous fûmes levés",
          "vous vous fûtes levés",
          "ils se furent levés"
        ]
      },
      "conditional": {
        "present": [
          "je me lèverais",
          "tu te lèverais",
          "il se lèverait",
          "nous nous lèverions",
          "vous vous lèveriez",
          "ils se lèveraient"
        ],
        "past": [
          "je me serais levé",
          "tu te serais levé",
          "il se serait levé",
          "nous nous serions levés",
          "vous vous seriez levés",
          "ils se seraient levés"
        ]
      },
      "subjunctive": {
        "present": [
          "que je me lève",
          "que tu te lèves",
          "qu'il se lève",
          "que nous nous levions",
          "que vous vous leviez",
          "qu'ils se lèvent"
        ],
        "imperfect": [
          "que je me levasse",
          "que tu te levasses",
          "qu'il se levât",
          "que nous nous levassions",
          "que vous vous levassiez",
          "qu'ils se levassent"
        ],
        "past": [
          "que je me sois levé",
          "que tu te sois levé",
          "qu'il se soit levé",
          "que nous nous soyons levés",
          "que vous vous soyez levés",
          "qu'ils se soient levés"
        ]
      },
      "imperative": {
        "imperative-present": [
          "lève-toi",
          "levons-nous",
          "levez-vous"
        ]
      },
      "participle": {
        "present-participle": [
          "se levant"
        ],
        "past-participle": [
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
    ("pouvoir", 200, expected_resp_conj_pouvoir),
    ("Pouvoir", 200, expected_resp_conj_pouvoir),
    ("pleuvoir", 200, expected_resp_conj_pleuvoir),
    ("Se lever", 200, expected_resp_conj_se_lever),
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
def test_read_search_infinitive(query, expected_status, expected_resp):
  response = client.get("/search/infinitive/{}".format(query))
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
