#!/usr/bin/env python
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

import verb_conjugate_fr.views
