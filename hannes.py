from fastapi import FastAPI,HTTPException 
from hannespydantic import Playerlist

app = FastAPI()

# Global storage for players, using player_number as key
all_playerlists = {}

@app.get("/")
async def root():
    return {"message": "Hello World This is hannes first FastApi"}

@app.get("/welcome")
async def root_results():
    return {"message": "Hello World This is hannes 1 "}

@app.post("/player" , status_code=201)
async def create_new_player(playerlist: Playerlist):
    # Use player_number as the key
    all_playerlists[playerlist.player_number] = playerlist
    return {
        "message": "Player info saved.",
        "see the list below for confirmation": playerlist
        
    }

@app.get("/allplayers")
async def get_all_players():
    return {
        "message": "Here we have all players",
        "playerlist": list(all_playerlists.values())
    }

@app.get("/player/{number}")
async def get_one_player_by_shirt_number(number: int):
    player = all_playerlists.get(number)

    if not player :
        raise HTTPException(status_code=404, detail="Players not found try annother shirt number")

    return { "message": f"here we found the {number}","see below for more details"
        "player_name": player.player_name,
        "previous_clubs": player.previous_clubs,
        "has_contract": player.has_contract,
        "question_formula": player.question_formula,
        "contract_expires": player.contract_expires,
        "player_number": player.player_number,
    }


@app.put("/player/{number}")
async def update_one_player_by_shirt_number(number: int,playerlist: Playerlist):
    player = all_playerlists.get(number)

    if not player :
        raise HTTPException(status_code=404, detail="Players not found try annother shirt number so you can update it")

       # Use player_number as the key
    all_playerlists[playerlist.player_number] = playerlist
    return {
        "message": "Player info saved and update at your request.",
        "see the list below for confirmation of the updated details": playerlist
        
    }

@app.delete("/player/{number}")
async def delete_one_player_by_shirt_number(number: int):
     if number not in all_playerlists:
       raise HTTPException(status_code=404, detail= f"Players with {number} not found try with annother number")
    
     deleted_player=all_playerlists.pop(number)
     return {
        "message": f"Player with shirt number {number} has been deleted.",
        "deleted_player": deleted_player,
        "see list you see the player is gone":all_playerlists
    }
    
    
