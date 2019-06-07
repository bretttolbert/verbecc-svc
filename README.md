# verb-conjugate-fr
Python microservice with REST API for conjugation of French verbs

Un microservice Python avec un API REST pour la conjugaison des verbes français

* Dockerized
* Unit tested
* Continuous Integration and Deployment with GitLab CI/CD

Usage Examples


http://localhost:8000/conjugate/mood/indicative/manger

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