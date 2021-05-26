from fastapi import APIRouter
from datetime import datetime, date
from pydantic import BaseModel

class DateOrdinal(BaseModel):
	ordinal: int
	date: date

router = APIRouter()

@router.get(
	'/fromordinal/{date_int}', 
	response_model=DateOrdinal, 
	summary='Get the date from ordinal date', 
	response_description="Ordinal integer and its corresponging date",
)
def from_ordinal(date_int:int):
	"""
	#From Orinal 
	Get the date from a Python Ordinal Interger
	
	date_int: Python integer date
	"""
	date = datetime.fromordinal(date_int)
	return {'ordinal':date_int,'date':date}

@router.get(
    '/toordinal/{date_str}', 
    response_model=DateOrdinal, 
    summary='Get the date from ordinal date', 
    response_description="Ordinal integer and its corresponging date",
)
def to_ordinal(date_str:date):
    """
    #From Orinal 
    Get the ordinal from a Python date
    
    date: Python date
    """
    return {'ordinal':date_str.toordinal(),'date':date_str}
