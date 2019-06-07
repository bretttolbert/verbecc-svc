#!/usr/bin/env python
from fastapi import FastAPI
app = FastAPI(title="verb-conjugate-fr")

import verb_conjugate_fr.views
