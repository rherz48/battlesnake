# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

# Princess Noodle Backstory (✿◕‿◕)
# Once upon a time in a far off planet there was a kingdom of snakes. It was a snake planet.
# It was a snake shaped planet with snakes. 
# Each year there was an epic (and i mean EPIC) battle TO THE DEATH for the snakes.
# To keep population levels down since there were a limited amount of apples to eat 
#
# Princess Noodle lived on this snake planet. (This fact was confirmed by snake reporters)
# Each year her older siblings came back from battle, blazing with victory, tearing through street as huge snake giants.
# She always felt so small and looked down upon. The garden snake in the family of dragons.
#
# But this year was her year to shine. To be the best and the baddest and the biggest snake around the snake planet.
# Princess Noodle had been trainning all year to:
    # 1. locate the best and juiciest apples
    # 2. sneak and slither past the other snakes
    # 3. Not get tangled around herself
# She was ready.
# Winning!!
# Princess Noodle won and totally demolished those other snakes.
# Now she is known around the snake shaped planet with snakes as Queen Noodle.

import random
import typing
import math


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "petraDeBat",  # TODO: Your Battlesnake Username
        "color": "#00cc00",  # TODO: Choose color
        "head": "dragon",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")

# # returns array of bad directions
# def floodfill(game_state: typing.Dict):
#     bad_moves = [] #determining this
#     my_head = game_state["you"]["body"][0]  # Coordinates of your head
#     my_neck = game_state["you"]["body"][1]  # coordinates of neck
#     print()

#     visited_list = []
#     to_check = []

#     unsafe_map = set()

#     for snake in game_state["snakes"]:
#         for body_part in snake["body"]:
#             unsafe_map.insert((body_part["x"], body_part["y"]))

    # if (3, 2) in unsafe_map:
        # we know this isn't safe

    # ......
    # ..hn..
    # ......

    for x in game_state["board"][]:
        my_head = 
    #1. create visited nodes list
    #2. to check list
    #3. 

    

    

    
    return bad_moves

# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"

    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        is_move_safe["up"] = False

    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']

    if(my_head["x"]+1 == board_width):
        is_move_safe["right"] = False
        
    elif (my_head["x"] == 0):
        is_move_safe["left"] = False

    if(my_head["y"]+1 == board_height):
        is_move_safe["up"] = False
    elif(my_head["y"] == 0):
        is_move_safe["down"] = False

    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself

    #HIIII
    #hello!!!!!
    
    my_body = game_state['you']['body']
    for snake in game_state['board']['snakes']:

      
        for segment in snake["body"]:

            if((my_head["x"] == segment["x"]+1) and (my_head["y"] == segment["y"])):
                is_move_safe["left"] = False
            elif((my_head["x"] == segment["x"]-1 ) and (my_head["y"] == segment["y"])):
                is_move_safe["right"] = False

            elif((my_head["y"] == segment["y"]-1 ) and (my_head["x"] == segment["x"])):
                is_move_safe["up"] = False
            elif((my_head["y"] == segment["y"]+1 ) and (my_head["x"] == segment["x"])):
                is_move_safe["down"] = False

        print(is_move_safe)


    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    # opponents = game_state['board']['snakes']

    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)
    print(safe_moves)

    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    # food = game_state['board']['food']
    my_health = game_state['you']['health']
    if(my_health < 101):
        try:
            nearest_food = game_state['board']['food'][0]
        except:
            nearest_food = 0
        for food in game_state['board']["food"]:
            if abs(food["x"] - my_head["x"] + food["y"] - my_head["y"]) < abs(nearest_food["x"] - my_head["x"] + nearest_food["y"] - my_head["y"]):
                nearest_food = food
        if nearest_food["x"] < my_head["x"] and is_move_safe["left"] == True:
            next_move = "left"
        elif nearest_food["x"] > my_head["x"] and is_move_safe["right"] == True:
            next_move = "right"
        elif nearest_food["y"] < my_head["y"] and is_move_safe["down"] == True:
            next_move = "down"
        elif nearest_food["y"] > my_head["y"] and is_move_safe["up"] == True:
            next_move = "up"

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
