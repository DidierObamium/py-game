import time
import keyboard

import utilities.index as util
import player.index as player
import world.index as world

if __name__ == "__main__":
    util.clearScreen()
    tick = True

    # Test zone, not game logic
    print("Hello, world!")
    player1 = player.Player(100.0, 2, 2)
    world_data = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
            ]
    
    while True:
        # First, we take care of the back-end world. Then, we display it.
        if tick:
            world_data[player1.ypos][player1.xpos] = "P"
            # Always this at the end
            util.clearScreen()
            world.showWorldData(world_data)
            world.showWorldMap(world_data)
            tick = False

        # Key bindings
        # 'Refresh' key
        if keyboard.is_pressed('r'):
            tick = True
            time.sleep(1/8)
        # 'Quit game' key
        if keyboard.is_pressed('q'):
            util.clearScreen()
            print("Quitting...")
            break
        # All of the movement keys
        # 'Move up' key
        if keyboard.is_pressed('w'):
            world_data[player1.ypos][player1.xpos] = 0 # Remove the player
            player1.ypos = player1.ypos - 1 # Change xpos
            if player1.ypos == -1: # If at the end of world, move to bottom
                player1.ypos = (len(world_data) - 1)
            tick = True
            time.sleep(1/8)
        # 'Move down' key
        if keyboard.is_pressed('s'):
            world_data[player1.ypos][player1.xpos] = 0 # Remove the player
            player1.ypos = player1.ypos + 1 # Change xpos
            if player1.ypos == len(world_data): # If at the end of world, move to top
                player1.ypos = 0
            tick = True
            time.sleep(1/8)
        # 'Move left' key
        if keyboard.is_pressed('a'):
            world_data[player1.ypos][player1.xpos] = 0 # Remove the player
            player1.xpos = player1.xpos - 1 # Change xpos
            if player1.xpos == -1: # If at the end of world, move to right
                player1.xpos = (len(world_data[player1.ypos]) - 1)
            tick = True
            time.sleep(1/8)
        # 'Move right' key
        if keyboard.is_pressed('d'):
            world_data[player1.ypos][player1.xpos] = 0 # Remove the player
            player1.xpos = player1.xpos + 1 # Change xpos
            if player1.xpos == len(world_data[player1.ypos]): # If at the end of world, move to right
                player1.xpos = 0
            tick = True
            time.sleep(1/8)