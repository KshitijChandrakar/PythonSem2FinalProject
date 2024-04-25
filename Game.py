from MyColors import *
from MyFunctions import *
import random, os
from ObjectClass import *
from buttons import *
from scene import *
from Attributes import *
# from movenet import *
print("RAAAAAAAAAAAAAH IM STARTING UP RAWr")
# from ObjectAttributes import *
clock = pygame.time.Clock()
movenetUsed = 0
def setHighScore():
    with open(highScoreFile, 'w') as file:
        file.write(str(environmentAttributes["highScore"]))

#---------------------------------------------------------------------------------------------------------------------------
# Setting up environment
font = pygame.font.Font(r"Gotham-Bold.otf", 32)  # Use default font, size 36
font2 = pygame.font.Font(r"Gotham-Bold.otf", 15)  # Use default font, size 36
font3 = pygame.font.Font(r"Gotham-Bold.otf", 24)  # Use default font, size 36
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
def setScore():
    environmentAttributes["score"] = 0
#--------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------
# #Defininig a few functions
def updateEnv():
    environmentAttributes["chanceOfSecond"] = map1(environmentAttributes["score"],0,environmentAttributes["MaxScore"], -0.1, 1)
    environmentAttributes["chanceOfThird"] = map1(environmentAttributes["score"],0,environmentAttributes["MaxScore"], -0.4, 1)
    pass
same = 0
jumping, lr, cur = 0,0,0
def checkEvent(event):
    jumping1 = 0
    global player, obstacle, same, jumping, lr, cur
    if event.type == pygame.QUIT:
        environmentAttributes["WindowRunning"] = False
    else:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    jumping = True
                    player.Force(player.Attributes["Jump"])
            if event.key == pygame.K_UP:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    jumping = True
                    player.Force(player.Attributes["Jump"])
            if event.key == pygame.K_LEFT:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    lr = -1
                    player.Force(player.Attributes["Move"] * -1)
            if event.key == pygame.K_RIGHT:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    lr = 1
                    player.Force(player.Attributes["Move"] * 1)
            if event.key == pygame.K_DOWN:
                jumping1 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    lr = 0
                    player.Force(player.Attributes["Move"] * 1)
            if event.key == pygame.K_RIGHT:
                if player.Attributes["pos"].y >= player.Attributes["rest"].y:
                    lr = 0
                    player.Force(player.Attributes["Move"] * -1)
        if jumping:
            if lr == -1:
                cur = 3
            elif lr == 1:
                cur = 4
        else:
            if jumping1 == 0:
                if lr == -1:
                    cur = 3
                elif lr == 1:
                    cur = 4
                else:
                    cur = 0
            else:
                cur = 0
                lr = 0



def centerText(centerTextStr, x_offset = 0, y_offset=0, color=white, font=font):
    # centerTextStr =
    centerText = font.render(centerTextStr, True, color)
    centerRect = centerText.get_rect()
    centerRect.center = width/2 + x_offset, height/2 + y_offset
    screen.blit(centerText, centerRect)
    return centerRect
    pass
def loadbg():
    global bg
    # print("Hi from bg")
    try:
        bg = pygame.transform.scale(pygame.image.load(environmentAttributes["GameBackgroundImage"]), (width, height))
    except KeyError:
        pass
def changeScene1(a,b):
    global currentScene, movenetUsed
    # print(environmentAttributes["score"])
    screen.fill((0,0,0))
    currentScene = a
    print(f"Changed Scene to {currentScene};", f"{"Not " if not b else ""}Using Movenet")
    movenetUsed = b
center = width/2, height/2

#--------------------------------------------------------------------------------------------------------------------------
#Rendering Fucntions
# button2 = Button(pos=(0, 0), Dimensions=(200, 200), text="Click Me", action=lambda: print("Button clicked!"), surface=environmentAttributes["screen"])
buttons, buttons1=[Button(),], [Button(),]
def handleStartScreenEvent(event):
    global buttons
    checkEvent(event)
    for i in buttons:
        i.handle_event(event)
def StartScreenInit():
    buttonWidth, buttonHeight = 200,50
    yoffset = -40
    ypadding = buttonHeight/2 + 30
    global buttons
    buttons = [
        Button(font = font2 ,rect = pygame.Rect(center[0] - buttonWidth/2, center[1]+ yoffset, buttonWidth, buttonHeight), text=f"{Button1Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"], action = changeScene1, actionParameters=("GameLoop",0), border_width=1),
        Button(font = font2, rect = pygame.Rect(center[0] - buttonWidth/2, center[1] + ypadding + yoffset,buttonWidth, buttonHeight), text=f"{Button2Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"], action = changeScene1, actionParameters=("GameLoop",1), border_width=1),
        Button(font = font2, rect = pygame.Rect(center[0] - buttonWidth/2, center[1] + ypadding * 2 + yoffset,buttonWidth, buttonHeight), text=f"{Button3Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"], action = sys.exit, actionParameters=(1, ), border_width=1),
    ]
    pass
def StartScreenUninit():
    global buttons
    del buttons
    centerText("loading...")
    pygame.display.flip()
    pass

def sameShit():
    global cur, same, player
    if cur != player.Attributes["CurrentSprite"]:
        player.Attributes["CurrentSprite"] = cur
        same = 0  # Reset the counter if the sprite changes
    else:
        # Increment the counter if the sprite remains unchanged
        same += 1

        # Check if the counter exceeds 20 frames
        if same >= 20:
            player.Attributes["CurrentSprite"] = 0  # Reset to 0 if it remains unchanged for 20 frames
            cur = 0
            same = 0  # Reset the counter
    # print(same)
def sameShit1():
    global cur
    player.Attributes["CurrentSprite"] = cur

def StartScreen():
    sameShit1()
    # print(player.Attributes["CurrentSprite"])
    global buttons
    # print("Hi From StartScreen")
    try:
        screen.blit(bg, (0,0))
    except KeyError:
        screen.fill(black)
    environmentAttributes["score"] += environmentAttributes["scoreSpeed"]
    TitleBox = centerText(f"{Title}", y_offset=-32 * 3.5, color=black)
    for i in buttons:
        i.run()
    # button2.run()
    player.run()

    pygame.display.flip()
    clock.tick(environmentAttributes["frameRate"])
    pass
def TestGameLoop():
    print("Hi from game loop")
    centerText("Runnning")
    pass
def handleGameOverScreenEvent(event):
    global buttons1
    for i in buttons1:
        i.handle_event(event)
def GameOverScreenInit():
    buttonWidth, buttonHeight = 200,50
    yoffset = 70
    ypadding = buttonHeight/2 + 30
    global buttons1
    buttons1 = [
        Button(font = font2 ,rect = pygame.Rect(buttonWidth/2, yoffset, buttonWidth, buttonHeight), text=f"{Button1Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"], action = changeScene1, actionParameters=("GameLoop",0), border_width=1),
        Button(font = font2, rect = pygame.Rect(buttonWidth/2, ypadding + yoffset,buttonWidth, buttonHeight), text=f"{Button2Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"], action = changeScene1, actionParameters=("GameLoop",1), border_width=1),
        Button(font = font2, rect = pygame.Rect(buttonWidth/2,  ypadding * 3 + yoffset,buttonWidth, buttonHeight), text=f"{Button4Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"],  action = changeScene1, actionParameters=("StartScreen",0), border_width=1),
        Button(font = font2, rect = pygame.Rect(buttonWidth/2, ypadding * 2 + yoffset,buttonWidth, buttonHeight), text=f"{Button3Text}",textColor=black, color = white + (70,),hover_color=white+(100,), surface=environmentAttributes["screen"], action = sys.exit, actionParameters=(1, ), border_width=1),
    ]
    pass
def GameOverScreenUninit():
    global buttons1
    del buttons1
    centerText("loading...")
    pygame.display.flip()
    pass

def GameOver():
    global buttons1
    # print("Hi From StartScreen")
    try:
        screen.blit(bg, (0,0))
    except KeyError:
        screen.fill(black)
    for i in buttons1:
        i.run()
    init = 4
    add = 1.25
    TitleBox = centerText(f"{GameOverText}",x_offset = 40, y_offset=-32 * init, color=black)
    ScoreTitleBox = centerText(f"Your Score: {environmentAttributes["score"]}", x_offset = 40, y_offset=-32 * (init-add), color=black,font=font3)
    hsTitleBox = centerText(f"High Score: {environmentAttributes["highScore"]}",x_offset = 40,  y_offset=-32 * (init-add*2), color=black,font=font3)
    pygame.display.flip()

    pass
def Won():
    centerText(f"{GameFinishedText}")
    pass
def loadMovenet():
    global movenet
    if movenetUsed:
        movenet = import_module("MovenetControls")
        movenet.OpenCamera()
    else:
        pass
def unloadmovenet():
    global movenet
    try:
        del movenet
    except NameError:
        pass
def GameLoop():
    if movenetUsed:
        movenet.whateverMovenetstuff(lambda : player.Force(player.Attributes["Jump"]))
    updateEnv()
    try:
        screen.blit(bg, (0,0))
    except KeyError:
        screen.fill(black)
    sameShit1()
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
    clock.tick(environmentAttributes["frameRate"])

    pass

#--------------------------------------------------------------------------------------------------------------------------
currentScene  = "StartScreen"
scenes = {}
def changeScene(a):
    global currentScene
    # print(environmentAttributes["score"])
    screen.fill((0,0,0))
    if scenes[currentScene].uninitialise != None:
        scenes[currentScene].uninitialise()
    currentScene = a
    print(f"Changed Scene to {currentScene}")
    return currentScene

scenes = {
    "StartScreen" : scene(StartScreen, eventFunction = handleStartScreenEvent, initialise=(loadbg, StartScreenInit), uninitialise=(StartScreenUninit, )),
    "GameLoop" : scene(GameLoop, excep = {"GameOver": (changeScene, "GameOver"), "Won": (changeScene, "Won")}, eventFunction = checkEvent, uninitialise=(resetEnv1,unloadmovenet), initialise=(setScore,  resetEnv, loadbg, loadMovenet)),
    "GameOver" : scene(GameOver, eventFunction = handleGameOverScreenEvent, initialise=(loadbg, GameOverScreenInit), uninitialise=(GameOverScreenUninit, )),
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
cap.release()
cv2.destroyAllWindows()
