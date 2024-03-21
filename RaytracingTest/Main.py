from pygameInit import *
from MyFunctions import *
width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "Dino without AI")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    # try:
    # screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
