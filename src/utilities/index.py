import os

def clearScreen():
    """
    Clears the screen according to the type of your OS.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

