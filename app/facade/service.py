from fastapi import FastAPI
from . import api

app = FastAPI(debug=True)
app.include_router(api.facade)