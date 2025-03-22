class Player:
    """
    Creates a new Player object, based on the given health:float, and both 
    xpos:int and ypos:int, position of the player, in 2D
    """
    def __init__(self, health:float, xpos:int, ypos:int):
        self.health = health
        self.xpos = xpos
        self.ypos = ypos