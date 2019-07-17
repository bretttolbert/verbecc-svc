#!/usr/bin/env python
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

__version__ = '1.5.3'

app = FastAPI(title='verbecc-svc')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

import verbecc_svc.views
