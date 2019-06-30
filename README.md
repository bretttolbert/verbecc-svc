# verb-conjugate-fr

### Python microservice with REST API for conjugation of French verbs

### Un microservice Python avec un API REST pour la conjugaison des verbes français

7000 verbs supported.

[![pipeline status](https://gitlab.com/bretttolbert/verb-conjugate-fr/badges/master/pipeline.svg)](https://gitlab.com/bretttolbert/verb-conjugate-fr/pipelines)

* Dockerized
* Unit tested
* Continuous Integration and Deployment with GitLab CI/CD
* Web Interface available: https://gitlab.com/bretttolbert/verb-conjugate-fr-web

## See it live
http://verbe.cc/vcfr/conjugate/manger

## Quick Start (Docker)
```
$ docker pull bretttolbert/verb-conjugate-fr:latest
$ docker run -d -p 8000:8000 bretttolbert/verb-conjugate-fr:latest
```

## Quick Start (Development)

```
$ make dev-build
$ make dev
```

## Credits
This package was created with the help of [Verbiste](https://perso.b2b2c.ca/~sarrazip/dev/verbiste.html), [FastAPI](https://github.com/tiangolo/fastapi), [uvicorn](https://github.com/encode/uvicorn), [starlette](https://github.com/encode/starlette), [lxml](https://github.com/lxml/lxml), [docker](https://docker.com), [docker-compose](https://docs.docker.com/compose/), [pytest](https://docs.pytest.org) and [python](https://www.python.org/).

## Usage Examples


* http://localhost:8000/conjugate/manger
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
      "infinitive": {
        "infinitive-present": [
          "manger"
        ]
      },
      "indicative": {
        "present": [
          "je mange",
          "tu manges",
          "il mange",
          "nous mangeons",
          "vous mangez",
          "ils mangent"
        ],
        "imperfect": [
          "je mangeais",
          "tu mangeais",
          "il mangeait",
          "nous mangions",
          "vous mangiez",
          "ils mangeaient"
        ],
        "future": [
          "je mangerai",
          "tu mangeras",
          "il mangera",
          "nous mangerons",
          "vous mangerez",
          "ils mangeront"
        ],
        "simple-past": [
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
        "pluperfect": [
          "j'avais mangé",
          "tu avais mangé",
          "il avait mangé",
          "nous avions mangé",
          "vous aviez mangé",
          "ils avaient mangé"
        ],
        "future-perfect": [
          "j'aurai mangé",
          "tu auras mangé",
          "il aura mangé",
          "nous aurons mangé",
          "vous aurez mangé",
          "ils auront mangé"
        ]
      },
      "conditional": {
        "present": [
          "je mangerais",
          "tu mangerais",
          "il mangerait",
          "nous mangerions",
          "vous mangeriez",
          "ils mangeraient"
        ],
        "past": [
          "j'aurais mangé",
          "tu aurais mangé",
          "il aurait mangé",
          "nous aurions mangé",
          "vous auriez mangé",
          "ils auraient mangé"
        ]
      },
      "subjunctive": {
        "present": [
          "que je mange",
          "que tu manges",
          "qu'il mange",
          "que nous mangions",
          "que vous mangiez",
          "qu'ils mangent"
        ],
        "imperfect": [
          "que je mangeasse",
          "que tu mangeasses",
          "qu'il mangeât",
          "que nous mangeassions",
          "que vous mangeassiez",
          "qu'ils mangeassent"
        ],
        "past": [
          "que j'aie mangé",
          "que tu aies mangé",
          "qu'il ait mangé",
          "que nous ayons mangé",
          "que vous ayez mangé",
          "qu'ils aient mangé"
        ]
      },
      "imperative": {
        "imperative-present": [
          "mange",
          "mangeons",
          "mangez"
        ]
      },
      "participle": {
        "present-participle": [
          "mangeant"
        ],
        "past-participle": [
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

* http://localhost:8000/find/infinitive/manger
```
{
  "value": {
    "infinitive": "manger",
    "template": "man:ger",
    "translation_en": "eat"
  }
}
```

* http://localhost:8000/search/infinitive/Se%20le
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

* http://localhost:8000/conjugate/mood/indicative/manger
```
{
  "value": {
    "present": [
      "je mange",
      "tu manges",
      "il mange",
      "nous mangeons",
      "vous mangez",
      "ils mangent"
    ],
    "imperfect": [
      "je mangeais",
      "tu mangeais",
      "il mangeait",
      "nous mangions",
      "vous mangiez",
      "ils mangeaient"
    ],
    "future": [
      "je mangerai",
      "tu mangeras",
      "il mangera",
      "nous mangerons",
      "vous mangerez",
      "ils mangeront"
    ],
    "simple-past": [
      "je mangeai",
      "tu mangeas",
      "il mangea",
      "nous mangeâmes",
      "vous mangeâtes",
      "ils mangèrent"
    ]
  }
}
```

* http://localhost:8000/find/conjugation-template/man:ger

