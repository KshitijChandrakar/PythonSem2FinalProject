from scene import *
from main import *

currentScene  = "StartScreen"
def changeScene(a):
    global currentScene
    currentScene = a
    print(f"Changed Scene to {currentScene}")
    return currentScene
scenes = {
    "StartScreen" : scene(StartScreen, event = {pygame.KEYDOWN : (changeScene, "GameLoop")}),
    "GameLoop" : scene(GameLoop, excep = {"GameOver": (changeScene, "GameOver")}, eventFunction = checkEvent),
    "GameOver" : scene(GameOver, event = {pygame.KEYDOWN : (changeScene, "StartScreen")})
}
# Main game loop
while True:
    # try:
    screen.fill((0,0,0))
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
        scenes[currentScene].render()
    except myException as E:
        scenes[currentScene].handleExp(E.id)
    pygame.display.flip()
    pass
