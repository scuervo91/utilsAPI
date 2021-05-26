from fastapi import FastAPI
from datetime import datetime, date
from pydantic import BaseModel

from routers import dates

app = FastAPI()

app.include_router(
	dates.router,
	prefix='/dates',
	tags=['dates']
)


@app.get("/")
def root():
	return {'dates':{'description':'Dates Utilities','path':'/dates'}}



