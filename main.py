from pygameInit import *
from myColors import *
from MyFunctions import *
import random, os
from ObjectClass import *


vector = pygame.math.Vector2
width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "Dino without AI")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(r"C:\Users\ASUS\Documents\University\sem2\Python\FinalProject\Idea 2\Gotham-Bold.otf", 32)  # Use default font, size 36



#---------------------------------------------------------------------------------------------------------------------------
# Setting up environment
environmentAttributes ={
    "Gravity" : vector(0,0.2),
    "width" : width,
    "height" : height,
    "screen" : screen,
    "score" : 0,
    "scoreSpeed" : 0.5,
    "MaxScore" : 9999,
    "WindowRunning" : True,
    "Won" : False,
    "GameRunning" : 0,
    "GameOver" : 0,
    "FirstRun" : 1,
}
playerAttributes = {
    "id" : "Player",
    "Collider" : True,
    "Constrain" : (True, True),
    "Constrain1" : vector(0,0),
    "Constrain2" : vector(width,height - 50),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(0,0),
    "Default" : vector(50, height - 50),
    "rest" : vector(50, height - 50),
    "Jump" : vector(0, -10),
    "randomise" : False,
    "Dimensions" : vector(30,50),
    "color" : color_grey,
    "Anti-Gravity" : False
}
obstacleAttributes = {
    "id" : "Obstacle0",
    "Collider" : False,
    "Constrain" : (True, True),
    "Constrain1" : vector(0,0),
    "Constrain2" : vector(width + 300,height),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(-4,0),
    "IncVelocity" : (True,False),
    "VelocityConstraints" : ((-4,-13),),
    "Default" : vector(width, height - 50),
    "rest" : vector(50, height - 50),
    "randomise" : True,
    "randomisationList" : [1,0],
    "randomisationConstrain" : [[width, width+200]],
    "Dimensions" : vector(30,50),
    "color" : (255,0,0),
    "Anti-Gravity" : True
}
obstacleAttributes1 = {
    "id" : "Obstacle1",
    "Collider" : False,
    "Constrain" : (True, True),
    "Constrain1" : vector(0,0),
    "Constrain2" : vector(width + 300,height),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(-4,0),
    "IncVelocity" : (True, False),
    "VelocityConstraints" : ((-4,-13),),
    "Default" : vector(width, height - 50),
    "rest" : vector(50, height - 50),
    "randomise" : True,
    "randomisationList" : [1,0],
    "randomisationConstrain" : [[width, width+200]],
    "Dimensions" : vector(30,50),
    "color" : (0,255,0),
    "Anti-Gravity" : True
}
obstacleAttributes2 = {
    "id" : "Obstacle2",
    "Collider" : False,
    "Constrain" : (True, True),
    "Constrain1" : vector(0,0),
    "Constrain2" : vector(width + 300,height),
    "DefaultAcceleration" : vector(0,0),
    "DefaultVelocity" : vector(-4,0),
    "IncVelocity" : (True,False),
    "VelocityConstraints" : ((-4,-13),),
    "Default" : vector(width, height - 50),
    "rest" : vector(50, height - 50),
    "randomise" : True,
    "randomisationList" : [1,0],
    "randomisationConstrain" : [[width, width+200]],
    "Dimensions" : vector(30,50),
    "color" : (0,0,255),
    "Anti-Gravity" : True
}
def resetEnv():
    global player, obstacle, obstacle1, obstacle2
    player = Box(playerAttributes, environmentAttributes)
    obstacle = Box(obstacleAttributes, environmentAttributes)
    obstacle1 = Box(obstacleAttributes1, environmentAttributes)
    obstacle2 = Box(obstacleAttributes2, environmentAttributes)
    environmentAttributes["Objects"] = (player, obstacle, obstacle1, obstacle2)
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_dir = os.path.dirname(script_path)

# Construct the absolute path of the input file
input_file_path = os.path.join(script_dir, 'highScore.txt')

# Read from the input file
with open(input_file_path, 'r') as file:
    environmentAttributes["highScore"] = int(float(file.read()))

resetEnv()
# obstacle1 = Box(obstacleAttributes, environmentAttributes) if random.rand() > 0.8 else None

# environmentAttributes["Objects"] = (player, obstacle)
#--------------------------------------------------------------------------------------------------------------------------

while environmentAttributes["WindowRunning"]:
    # checkQuit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            environmentAttributes["WindowRunning"] = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # print(len(removeNone(environmentAttributes["Objects"])))
            # print(player.environmentAttributes["Gravity"], player.Attributes["pos"])
            # obstacle.debug()
            # obstacle1.debug()
            # obstacle2.debug()
            if environmentAttributes["FirstRun"]:
                print("Running for first time")
                environmentAttributes["FirstRun"] = False
                environmentAttributes["GameRunning"] = True

            if environmentAttributes["GameOver"] or environmentAttributes["Won"]:
                print("Restarting Game")
                environmentAttributes["GameOver"] = False
                environmentAttributes["Won"] = False
                environmentAttributes["GameRunning"] = True
                del player, obstacle
                environmentAttributes["score"] = 0
                resetEnv()
                # player.debug()
                # obstacle.debug()
            else:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    # print("Jumping")
                    player.Force(player.Attributes["Jump"])
            pass

    screen.fill(black)
    sco = int(round(environmentAttributes["score"], -1))
    scoreText = font.render(f"Score: {sco}", True, white)
    scoreRect = scoreText.get_rect()
    scoreRect.center = width - scoreRect.width/2 - 30, 30

    hsco = int(round(environmentAttributes["highScore"], -1))
    hscoreText = font.render(f"High Score: {hsco}", True, white)
    hscoreRect = scoreText.get_rect()
    hscoreRect.center = scoreRect.width/2 + 30, 35
    # pygame.draw.line(environmentAttributes["screen"], white, (0,30), (width, 30))
    centerTextStr = "Press Space To Start" if environmentAttributes["FirstRun"] else "You Won!!!" if environmentAttributes["Won"] else "Game Over" if environmentAttributes["GameOver"] else ""
    centerText = font.render(centerTextStr, True, white)
    centerRect = centerText.get_rect()
    centerRect.center = width/2, height/2
    screen.blit(centerText, centerRect)

    #Check if game is still running
    if environmentAttributes["GameRunning"]:
        screen.blit(scoreText, scoreRect)

        screen.blit(hscoreText, hscoreRect)
        #Run it ALl
        for i in environmentAttributes["Objects"]:
            if i != None:
                i.run()
                if i.checkCollision(removeNoneItem(environmentAttributes["Objects"], i)):
                    with open(input_file_path, 'w') as file:
                        file.write(str(environmentAttributes["highScore"]))
                    print("Game Over by Collision of", i.Attributes["id"])
                    environmentAttributes["GameOver"] = True
                    environmentAttributes["GameRunning"] = False
                    break
        #Check if environmentAttributes["Won"]
        if environmentAttributes["score"] >= environmentAttributes["MaxScore"]:
            environmentAttributes["GameRunning"] = False
            environmentAttributes["Won"] = True
        #If game not over then add score
        if not environmentAttributes["GameOver"]:

            environmentAttributes["score"] += environmentAttributes["scoreSpeed"]
            if environmentAttributes["score"] > environmentAttributes["highScore"]:
                environmentAttributes["highScore"] = environmentAttributes["score"]

    pygame.display.flip()
    clock.tick(80)

pygame.quit()
sys.exit()
