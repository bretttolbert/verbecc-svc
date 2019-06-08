#!/usr/bin/env python
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title='verb-conjugate-fr')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

import verb_conjugate_fr.views
