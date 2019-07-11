## verbecc

#### Verbs, completely conjugated - French and Spanish verb conjugator

#### Verbes, complètement conjugués - conjugaison en français et espagnol

#### Verbos, completamente conjugados - conjugador de verbos francés y español

https://github.com/bretttolbert/verbecc

[![Python Package Index Status](https://img.shields.io/pypi/v/verbecc.svg)](https://pypi.python.org/pypi/verbecc) [![GitLab CI pipeline status](https://gitlab.com/bretttolbert/verbecc/badges/master/pipeline.svg)](https://gitlab.com/bretttolbert/verbecc/pipelines)

#### Features
* Over 7,000 French verbs and 9,000 Spanish verbs supported
* pip installable
* Unit tested
* Continuous Integration and Deployment with GitLab CI/CD
* Dependencies: lxml

#### Credits
Created with the help of [lxml](https://github.com/lxml/lxml), [pytest](https://docs.pytest.org) and [python](https://www.python.org/). French verb conjugation template XML files derived from [Verbiste](https://perso.b2b2c.ca/~sarrazip/dev/verbiste.html) and Spanish verb conjugation XML files dervied from [mlconjug](https://github.com/SekouD/mlconjug).

## verbecc-svc

#### verbecc-svc Microservice Python avec un API REST pour la conjugaison des verbes français

#### verbecc-svc Python microservice with REST API for conjugation of French verbs

https://github.com/bretttolbert/verbecc-svc

[![pipeline status](https://gitlab.com/bretttolbert/verb-conjugate-fr/badges/master/pipeline.svg)](https://gitlab.com/bretttolbert/verb-conjugate-fr/pipelines)

#### Live demo
http://verbe.cc/vcfr/conjugate/manger

#### Features
* Dockerized microservice
* Unit tested
* Continuous Integration and Deployment with GitLab CI/CD
* RESTful API with JSON responses
* Dependencies: verbecc

#### Credits
Created with the help of [verbecc](https://github.com/bretttolbert/verbecc), [FastAPI](https://github.com/tiangolo/fastapi), [uvicorn](https://github.com/encode/uvicorn), [starlette](https://github.com/encode/starlette), [docker](https://docker.com), [docker-compose](https://docs.docker.com/compose/), [pytest](https://docs.pytest.org) and [python](https://www.python.org/).


## verbecc-web

#### Une interface web pour verbecc-svc

#### Web front-end for verbecc-svc

https://github.com/bretttolbert/verbecc-web

#### Live demo
http://verbe.cc

#### Features
* Dockerized
* Search suggestions
* Implemented entirely in Javascript (JQuery) - conjugations are generated without reloading the page
* Dependencies: verbecc-svc

#### Credits
Created with the help of [verbecc-svc](https://github.com/bretttolbert/verbecc-svc), and [JQuery](https://jquery.com/)


```
+------------------------------------------------------+                                                                               
|               verbecc-web                            |                                                                               
|               web application                        |                                                                               
|               docker-compose                         |                                                                               
|                      |                               |                                                                               
|                  REST API                            |                                                                               
|                      |                               |                                                                               
|      +----------------------------------------+      |                                                                               
|      |                                        |      |                                                                               
|      |       verbecc-svc                      |      |                                                                               
|      |       Dockerized microservice          |      |                                                                               
|      |                                        |      |                                                                               
|      |        +----------------------+        |      |                                                                               
|      |        |   verbecc            |        |      |                                                                               
|      |        |   Python library     |        |      |                                                                               
|      |        +----------------------+        |      |                                                                               
|      +----------------------------------------+      |                                                                               
+------------------------------------------------------+                                                                               
```   


# verbecc-svc

#### Quick Start (Docker)
```
$ docker pull bretttolbert/verbecc-svc:latest
$ docker run -d -p 8000:8000 bretttolbert/verbecc-svc:latest
```

## Quick Start (Development)

```
$ make dev-build
$ make dev
```

## Usage Examples

* http://localhost:8000/conjugate/fr/manger
```
{
  "value": {
    "verb": {
      "infinitive": "manger",
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
```

* http://localhost:8000/conjugate/fr/se+lever
```
{
  "value": {
    "verb": {
      "infinitive": "lever",
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
```

* http://localhost:8000/find/infinitive/fr/manger
```
{
  "value": {
    "infinitive": "manger",
    "template": "man:ger",
    "translation_en": "eat"
  }
}
```

* http://localhost:8000/search/infinitive/fr/Se+le
```
{
  "value": [
    "se lécher",
    "se léchouiller",
    "se légaliser",
    "se légender",
    "se légiférer",
    "se légitimer",
    "se léguer",
    "se lénifier",
    "se léser",
    "se lésiner"
  ]
}
```

* http://localhost:8000/conjugate/fr/manger?mood=indicatif
```
{
  "value": {
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
  }
}
```

* http://localhost:8000/conjugate/fr/manger?mood=indicatif&tense=passé-composé
```
{
  "value": [
      "j'ai mangé",
      "tu as mangé",
      "il a mangé",
      "nous avons mangé",
      "vous avez mangé",
      "ils ont mangé"
    ]
}
```

* http://localhost:8000/find/conjugation-template/fr/man:ger
* http://localhost:8000/find/conjugation-template/es/deb:er
