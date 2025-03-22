def showWorldData(world_data:list[list]):
    """
    Input: world:[list[list]], current world.
    Prints the current worldmap to the screen, line by line.
    """
    for index in range(len(world_data)):
        print(world_data[index])