from pygameInit import *
from pygame.math import Vector2 as vector
from MyColors import *
from MyFunctions import *
import os
from spritesheet import SpriteSheet
width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "Dino with AI")
screen = pygame.display.set_mode((width, height))

def gameOverFunc(i):
    print("Game Over by Collision of", i.Attributes["id"])
    environmentAttributes["GameOver"] = True
    # environmentAttributes["GameRunning"] = False
    raise myException("GameOver")
    pass
Title = "Ball Dodger"
GameOverText = "Game Over"
GameFinishedText = "You won"
Button1Text, Button2Text, Button3Text, Button4Text = "Run Without Movenet","Run With Movenet", "Quit", "Back To Start Screen"
environmentAttributes ={
    "GameBackgroundImage" : "resources/Background.png",
    "Gravity" : vector(0,0.2),
    "width" : width,
    "height" : height,
    "frameRate" : 40,
    "screen" : screen,
    "score" : 0,
    "scoreSpeed" : 0.5,
    "MaxScore" : 99999,
    "WindowRunning" : True,
    "chanceOfSecond" : 1 - 0.6,
    "chanceOfThird" : 1 - 0.3,

}
playerAttributes = {
    "id" : "Player",
    "Render" : True,
    "Update" : True,
    "Collider" : True,
    "CollisionFunction" : gameOverFunc,
    "Constrain" : (True, True),
    "Constrain1" : vector(0,0),
    "Constrain2" : vector(width,height - 70),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(0,0),
    "Default" : vector(width - 100, height - 68),
    "rest" : vector(width - 100, height - 68),
    "Jump" : vector(0, -11.5),
    "randomise" : (False,False),
    "Dimensions" : vector(80,68),
    "color" : color_grey,
    "Anti-Gravity" : False,
    # "Image" : ["resources/Obstacle.png",],
    # "Sprites" : SpriteSheet("resources/cat.png"),
    "Sprites" : (SpriteSheet("resources/catrest.png"), SpriteSheet("resources/catwalkleft.png"),SpriteSheet("resources/catwalkright.png"),SpriteSheet("resources/catrunleft.png"),SpriteSheet("resources/catrunright.png")),
    "changeFrameCount": (4,4,4,4,4),
    "RowAndColumn" : ((1, 3),(1, 6),(1, 6),(1, 6),(1, 6)),
    "Padding" : ((0,0),(0,0),(0,0),(0,0),(0,0)),
    "Margin" : ((0,0),(0,0),(0,0),(0,0),(0,0)),
    "Debug" : 0,
    "RevA" : 0,
    "Move" : vector(5,0),
    "SwitchSprites" : True,
    "CurrentSprite" : 0
}
def rev(self):

    pass
idk = 1
obstacleAttributes = {
    "id" : "Obstacle0",
    "Render" : True,
    "Update" : True,
    # "Collider" : False,
    # "CollisionFunction" : rev,
    "Constrain" : (True, True),
    "Constrain1" : vector(-2000,0),
    "Constrain2" : vector(width, height),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(5 * idk,0),
    "IncVelocity" : (True,False),
    "VelocityConstraints" : ((4 * idk,9 * idk),),
    "Default" : vector(0, height - 200),
    "rest" : vector(0, height - 200),
    "randomise" : [1, 0],
    "randomisationList" : [1,0],
    "randomisationConstrain" : [[-2000, 0]],
    "Dimensions" : vector(50,50),
    "color" : (255,0,0),
    "Image" : ["resources/snowball.png",],
    # "Sprites" : SpriteSheet("resources/obstacle.png"),
    # "changeFrameCount": 4,
    # "RowAndColumn" : (2, 4),
    # "Padding" : (0,0),
    # "Margin" : (0,0),
    "changeFrameCount": 6,
    "Anti-Gravity" : False,
    "Rev" : -1,
    "RevA" : 1
    # "Debug" : True

}
