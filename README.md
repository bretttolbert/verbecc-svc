# verb-conjugate-fr

### Python microservice with REST API for conjugation of French verbs

### Un microservice Python avec un API REST pour la conjugaison des verbes français

7000 verbs supported.

[![pipeline status](https://gitlab.com/bretttolbert/verb-conjugate-fr/badges/master/pipeline.svg)](https://gitlab.com/bretttolbert/verb-conjugate-fr/pipelines)

* Dockerized
* Unit tested
* Continuous Integration and Deployment with GitLab CI/CD
* Web Interface available: https://gitlab.com/bretttolbert/verb-conjugate-fr-web

## Live Demo
http://142.93.74.193/conjugate/manger

## Quick Start (Docker)
```
$ docker login registry.gitlab.com
$ docker pull registry.gitlab.com/bretttolbert/verb-conjugate-fr
$ docker run --name verb_conjugate_fr -d -p 8000:8000 bretttolbert/verb-conjugate-fr:latest
```

## Quick Start (Development)

```
$ make dev-build && make dev
```

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
