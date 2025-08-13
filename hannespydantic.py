from pydantic import BaseModel

from datetime import date ## import date structure class from module datedime 

class Playerlist(BaseModel):
    player_name:str
    previous_clubs:list[str]
    has_contract:bool
    question_formula:dict[str,bool]
    contract_expires:date| None 
    player_number:int
    