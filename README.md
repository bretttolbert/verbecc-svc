# verb-conjugate-fr
Python French verb conjugation / Conjugaison des verbes français en Python

* Unit tested
* Travis CI ![Travis CI build status](https://travis-ci.org/bretttolbert/verb-conjugate-fr.svg?branch=master)
* Currently under development
* Has a command line interface
* Coming soon: Flask web interface

Build with setup.py or use tox to build (both py27 and p3) and run unit tests and linters.

```
brett@ubuntu:~/Git/verb-conjugate-fr$ tox
...
brett@ubuntu:~/Git/verb-conjugate-fr$ source .py3/bin/activate
(.py3) brett@ubuntu:~/Git/verb-conjugate-fr$ confr manger
<lxml.etree._ElementTree object at 0x7fce6c9200c8>
<Element verbs-fr at 0x7fce6c9206c8>
loaded 7000 verbs
<lxml.etree._ElementTree object at 0x7fce6c6e1fc8>
<Element conjugation-fr at 0x7fce6c6e1f88>
loaded 132 conjugation templates
Conjugaison du verbe manger
Template: man:ger

je mange
tu manges
il mange
nous mangeons
vous mangez
ils mangent

Entrez un mot français pour conjuguer
Enter a French verb to conjugate
foo
Aucune mot trouvé
Verb not found
No matches
Entrez un mot français pour conjuguer
Enter a French verb to conjugate
cro
Aucune mot trouvé
Verb not found
Matches:
croasser
crocher
crocheter
crochir
croire
croiser
croquer
crosser
crotter
crouler
croupir
croustiller
croître
croûter
Entrez un mot français pour conjuguer
Enter a French verb to conjugate
```
