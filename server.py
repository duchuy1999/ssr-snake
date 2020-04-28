import os
import random

import cherrypy

from tools import find_food, get_dir

BODY = 0
EMPTY = 1
FOOD = 2
"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    @cherrypy.expose
    def index(self):
        # If you open your snake URL in a browser you should see this message.
        return "Your Battlesnake is alive!"

    @cherrypy.expose
    def ping(self):
        # The Battlesnake engine calls this function to make sure your snake is working.
        return "pong"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        # TODO: Use this function to decide how your snake is going to look on the board.
        data = cherrypy.request.json
        print("START")
        return {"color": "#888888", "headType": "regular", "tailType": "regular"}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json

        height = data["board"]["height"]
        width = data["board"]["width"]
        board = [[EMPTY for i in range(height)] for j in range(width)]
        food_list = []

        for food in data["board"]["food"]:
            board[food["x"]][food["y"]] = FOOD
            food_list.append((food["x"], food["y"]))

        for snakes in data["board"]["snakes"]:
            for body in snakes["body"]:
                board[body["x"]][body["y"]] = BODY

        directions = ["up", "down", "left", "right"]
        move = "up"

        myHeadX = data["you"]["body"][0]["x"]
        myHeadY = data["you"]["body"][0]["y"]
        myHead = (myHeadX, myHeadY)
        myHealth = data["you"]["health"]

        grid_on_path = find_food(board, food_list, myHead)
        print(grid_on_path)
        if grid_on_path == None:
            # Avoid walls and bodies, make this def IsWall later
            if myHeadX - 1 < 0 or board[myHeadX - 1][myHeadY] == BODY:
                directions.remove("left")
            if myHeadX + 1 >= width or board[myHeadX + 1][myHeadY] == BODY:
                directions.remove("right")
            if myHeadY - 1 < 0 or board[myHeadX][myHeadY - 1] == BODY:
                directions.remove("up")
            if myHeadY + 1 >= height or board[myHeadX][myHeadY + 1] == BODY:
                directions.remove("down")
            if len(directions) != 0:
                move = random.choice(directions)

        else:
            if get_dir(myHead, grid_on_path) != None:
                move = get_dir(myHead, grid_on_path)

        """
        #Avoid walls and bodies, make this def IsWall later
        if myHeadX - 1 < 0 or board[myHeadX - 1][myHeadY] == BODY:
            directions.remove("left")
        if myHeadX + 1 >= width or board[myHeadX + 1][myHeadY] == BODY:
            directions.remove("right")
        if myHeadY - 1 < 0 or board[myHeadX][myHeadY - 1] == BODY:
            directions.remove("up")
        if myHeadY + 1 >= height or board[myHeadX][myHeadY + 1] == BODY:
            directions.remove("down")

        if len(directions) == 0:
            move = "up"
        else:
            move = random.choice(directions)
        """

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json
        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
