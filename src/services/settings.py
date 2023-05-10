"""Customizable settings for the game.
Changing the attributes is not tested, and if changed incorrectly it might result in
the game crashing. If you can not remember the correct format for this file,
please download it again from the github page.

Attributes:
    FPS: Indicates how many times in a frame the game updates. Both the 
    screen and the logic will be updated this many times in a second.
    TILESIZE: Tells how many pixels large each image in the assets folder is.
    All images in the folder must be the same size.
    TURNS: Tells how many turns the game should have.
    MAP: A layout of the games arena.
"""

FPS = 60
TILESIZE = 64
TURNS = 30

MAP = [
    ["x", "x", "x", "x", "x", "x", "x", "x",
        "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", "p1gu", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", "p2gu", " ", "x"],
    ["x", " ", "p1g", " ", "p1flag", "p1", " ", " ",
        " ", " ", "p2", "p2flag", " ", "p2g", " ", "x"],
    ["x", " ", "p1gl", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", "p2gl", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x",
        "x", "x", "x", "x", "x", "x", "x", "x"]
]
