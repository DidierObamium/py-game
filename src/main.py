import time

import utilities.index as util
import player.index as player
import world.index as world

if __name__ == "__main__":
    util.clearScreen()
    tick = True

    # Test zone, not game logic
    print("Hello, world!")
    player1 = player.Player(100.0, 0, 0)
    world_data = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
            ]
    
    while True:
        if tick:
            world_data[player1.xpos][player1.ypos] = "P"
            # Always this at the end
            util.clearScreen()
            world.showWorldData(world_data)
            tick = False