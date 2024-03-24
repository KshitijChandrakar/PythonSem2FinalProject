from myColors import *
from MyFunctions import *
import random, os
from ObjectClass import *
from scene import *
from Attributes import *

print("RAAAAAAAAAAAAAH IM STARTING UP RAWr")
# from ObjectAttributes import *
clock = pygame.time.Clock()

def setHighScore():
    with open(highScoreFile, 'w') as file:
        file.write(str(environmentAttributes["highScore"]))

#---------------------------------------------------------------------------------------------------------------------------
# Setting up environment
font = pygame.font.Font(r"Gotham-Bold.otf", 32)  # Use default font, size 36
def resetEnv():
    global player, obstacle, obstacle1, obstacle2
    player = Box(playerAttributes.copy(), environmentAttributes)
    obstacle = Box(obstacleAttributes.copy(), environmentAttributes)
    obstacle1 = Box(editCopyDict(obstacleAttributes, {"color" : (0,255,0)}), environmentAttributes) if random.random() > environmentAttributes["chanceOfSecond"] else None
    obstacle2 = Box(editCopyDict(obstacleAttributes, {"color" : (0,0,255)}), environmentAttributes) if random.random() > environmentAttributes["chanceOfThird"] else None

    environmentAttributes["Objects"] = (player, obstacle, obstacle1, obstacle2)
    environmentAttributes["score"] = 0
script_dir = os.path.dirname(os.path.abspath(__file__))
highScoreFile = os.path.join(script_dir, 'highScore.txt')
# Read from the input file
with open(highScoreFile, 'r') as file:
    environmentAttributes["highScore"] = int(float(file.read()))
def resetEnv1():
    resetEnv()
    setHighScore()
resetEnv()
# obstacle1 = Box(obstacleAttributes, environmentAttributes) if random.rand() > 0.8 else None


# environmentAttributes["Objects"] = (player, obstacle)
#--------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------
#Defininig a few functions
def updateEnv():
    environmentAttributes["chanceOfSecond"] = map(environmentAttributes["score"],0,environmentAttributes["MaxScore"], -0.1, 1)
    environmentAttributes["chanceOfThird"] = map(environmentAttributes["score"],0,environmentAttributes["MaxScore"], -0.4, 1)
    pass
def checkEvent(event):
    global player, obstacle
    if event.type == pygame.QUIT:
        environmentAttributes["WindowRunning"] = False
    else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #
            # if environmentAttributes["GameOver"] or environmentAttributes["Won"]:
            #     print("Restarting Game")
            #     environmentAttributes["GameOver"] = False
            #     environmentAttributes["Won"] = False
            #     environmentAttributes["GameRunning"] = True
            #     del player, obstacle
            #     environmentAttributes["score"] = 0
            #     resetEnv()
                # player.debug()
                # obstacle.debug()
            # else:
            if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                # print("Jumping")
                player.Force(player.Attributes["Jump"])
            # pass
def centerText(centerTextStr):
    # centerTextStr =
    centerText = font.render(centerTextStr, True, white)
    centerRect = centerText.get_rect()
    centerRect.center = width/2, height/2
    screen.blit(centerText, centerRect)
    pass
def StartScreen():
    # print("Hi From StartScreen")
    centerText("Press Space to Play")

    pass
def TestGameLoop():
    print("Hi from game loop")
    centerText("Runnning")
    pass
def loadbg():
    global bg
    try:
        bg = pygame.transform.scale(pygame.image.load(environmentAttributes["GameBackgroundImage"]), (width, height))
    except KeyError:
        pass

def GameLoop():
    # print("Hi From Game Loop")
    # while environmentAttributes["WindowRunning"]:
    # for event in pygame.event.get():
    #     checkEvent(event)
    updateEnv()
    try:
        screen.blit(bg, (0,0))
    except KeyError:
        screen.fill(black)

    # pygame.draw.line(environmentAttributes["screen"], white, (0,30), (width, 30))
    # "Press Space To Start" if environmentAttributes["FirstRun"]\
    #      else "You Won!!!" if environmentAttributes["Won"]\
    #      else "Game Over Press Space To Restart" if environmentAttributes["GameOver"]\
    #      else ""
    # centerText("Running")
    #Check if game is still running
    # if environmentAttributes["GameRunning"]:
        # print("Game Is RUnnning")
    #-----------------------------------------------------------------------------
    #Rendering Scores
    sco = int(round(environmentAttributes["score"], -1))
    scoreText = font.render(f"Score: {sco}", True, white)
    scoreRect = scoreText.get_rect()
    scoreRect.center = width - scoreRect.width/2 - 30, 30
    hsco = int(round(environmentAttributes["highScore"], -1))
    hscoreText = font.render(f"High Score: {hsco}", True, white)
    hscoreRect = scoreText.get_rect()
    hscoreRect.center = scoreRect.width/2 + 30, 35
    screen.blit(scoreText, scoreRect)
    screen.blit(hscoreText, hscoreRect)
    #-----------------------------------------------------------------------------
    #Run it ALl for all objects

    for i in environmentAttributes["Objects"]:
        if i != None:
            i.run()
            # if i.checkCollision(removeNoneItem(environmentAttributes["Objects"], i)):
            #     i.onCollision()
    #Check if environmentAttributes["Won"]
    if environmentAttributes["score"] >= environmentAttributes["MaxScore"]:
        environmentAttributes["GameRunning"] = False
        environmentAttributes["Won"] = True
    #If game not over then add score
    # if not environmentAttributes["GameOver"]:

    environmentAttributes["score"] += environmentAttributes["scoreSpeed"]
    if environmentAttributes["score"] >= environmentAttributes["MaxScore"]:
        raise myException("Won")
    if environmentAttributes["score"] > environmentAttributes["highScore"]:
        environmentAttributes["highScore"] = environmentAttributes["score"]
    pygame.display.flip()
    clock.tick(80)

    pass
def GameOver():
    centerText("Game Over")
    pass
def Won():
    centerText("You Won!!!")
    pass
#--------------------------------------------------------------------------------------------------------------------------

currentScene  = "StartScreen"
def changeScene(a):
    global currentScene
    # print(environmentAttributes["score"])
    screen.fill((0,0,0))
    if scenes[currentScene].uninitialse != None:
        scenes[currentScene].uninitialse()
    currentScene = a
    print(f"Changed Scene to {currentScene}")
    return currentScene
scenes = {
    "StartScreen" : scene(StartScreen, event = {pygame.KEYDOWN : (changeScene, "GameLoop")}),
    "GameLoop" : scene(GameLoop, excep = {"GameOver": (changeScene, "GameOver"), "Won": (changeScene, "Won")}, eventFunction = checkEvent, uninitialse=resetEnv1, initialise=(resetEnv, loadbg)),
    "GameOver" : scene(GameOver, event = {pygame.KEYDOWN : (changeScene, "StartScreen")}),
    "Won" : scene(Won, event = {pygame.KEYDOWN : (changeScene, "StartScreen")}),
}
# Main window loop
while True:
    # try:
    # screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            #print(event)
            if scenes[currentScene].events != None:
                scenes[currentScene].handleEvent(event.type)
            if scenes[currentScene].eventFunction != None:
                scenes[currentScene].eventFunction(event)
            # print(currentScene)
    # finally:

    try:
        if not scenes[currentScene].Initialised:
            scenes[currentScene].Initialised = 1
            if scenes[currentScene].initialise != None:
                scenes[currentScene].initialise()
        scenes[currentScene].render()
    except myException as E:
        scenes[currentScene].handleExp(E.id)
    pygame.display.flip()
    pass
