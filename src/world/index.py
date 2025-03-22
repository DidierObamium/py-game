def showWorldData(world_data:list[list]):
    """
    Input: world:[list[list]], current world's data.
    Prints the current world's datamap to the screen, line by line.
    """
    for index in range(len(world_data)):
        print(world_data[index])

def showWorldMap(world_data:list[list]):
    """
    Input: world:[list[list]], current world's data.
    Prints the current worldmap to the screen.
    """
    printed_world = [
        ["□", "□", "□", "□", "□"],
        ["□", "□", "□", "□", "□"],
        ["□", "□", "□", "□", "□"],
        ["□", "□", "□", "□", "□"],
        ["□", "□", "□", "□", "□"]
    ]
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] == "P": # If the player is on that square
                printed_world[i][j] = "▼"
    shown_line = ""
    for i in range(len(printed_world)):
        for j in range(len(printed_world[i])):
            shown_line += printed_world[i][j]
        print(shown_line)
        shown_line = ""