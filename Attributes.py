from pygameInit import *
from pygame.math import Vector2 as vector
from myColors import *
from MyFunctions import *
import os
width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "Dino without AI")
screen = pygame.display.set_mode((width, height))

def gameOverFunc(i):
    print("Game Over by Collision of", i.Attributes["id"])
    environmentAttributes["GameOver"] = True
    # environmentAttributes["GameRunning"] = False
    raise myException("GameOver")
    pass

environmentAttributes ={
    "GameBackgroundImage" : "resources/ima.jpeg",
    "Gravity" : vector(0,0.2),
    "width" : width,
    "height" : height,
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
    "Default" : vector(50, height - 70),
    "rest" : vector(50, height - 70),
    "Jump" : vector(0, -11.5),
    "randomise" : False,
    "Dimensions" : vector(50,70),
    "color" : color_grey,
    "Anti-Gravity" : False,
    "Image" : ["resources/Dino.png", "resources/Dino1.png"],
    "changeFrameCount": 6
}
obstacleAttributes = {
    "id" : "Obstacle0",
    "Render" : True,
    "Update" : True,
    # "Collider" : False,
    "Constrain" : (True, True),
    "Constrain1" : vector(0,0),
    "Constrain2" : vector(width + 2000,height),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(-4,0),
    "IncVelocity" : (True,False),
    "VelocityConstraints" : ((-4,-20),),
    "Default" : vector(width, height - 70),
    "rest" : vector(50, height - 50),
    "randomise" : True,
    "randomisationList" : [1,0],
    "randomisationConstrain" : [[width, width+2000]],
    "Dimensions" : vector(50,70),
    "color" : (255,0,0),
    "Image" : ["resources/Obstacle.png",],
    "changeFrameCount": 6,
    "Anti-Gravity" : True
}
