import pygame
import sys
def emptyFunction(*args):
    pass
#Hypo = sqrt((x(b/a+b))^2 + ((a/a+b)x)^2)
def checkQuit(function = emptyFunction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            function(event)

def startPygame(hypo = 300, ratioa = 16, ratiob = 9, caption = "Default Pygame"):
    global screen
    pygame.init()
    x = (ratioa + ratiob) * hypo / ((ratioa ** 2 + ratiob ** 2) ** 0.5)
    pygame.display.set_caption(caption)
    return (ratioa/(ratioa + ratiob)) * x, (ratiob/(ratioa + ratiob)) * x
