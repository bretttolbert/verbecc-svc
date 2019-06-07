# verb-conjugate-fr

### Python microservice with REST API for conjugation of French verbs

### Un microservice Python avec un API REST pour la conjugaison des verbes français

7000 verbs supported.

[![pipeline status](https://gitlab.com/bretttolbert/verb-conjugate-fr/badges/master/pipeline.svg)](https://gitlab.com/bretttolbert/verb-conjugate-fr/pipelines)

* Dockerized
* Unit tested
* Continuous Integration and Deployment with GitLab CI/CD

**This project is WIP and is NOT production ready!**

## Quick Start (Development)

```
make dev-build && make dev
```

## Usage Examples

http://localhost:8000/conjugate/manger

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

http://localhost:8000/find/infinitive/manger
```
{
  "value": {
    "infinitive": "manger",
    "template": "man:ger",
    "translation_en": "eat"
  }
}
```

http://localhost:8000/conjugate/mood/indicative/manger
http://localhost:8000/find/conjugation-template/man:ger
