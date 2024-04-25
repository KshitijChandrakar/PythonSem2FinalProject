from pygameInit import *
# width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "Dino with AI")
# screen = pygame.display.set_mode((width, height))

from MyColors import *
pygame.font.init()
class Button:
    hovered = False
    def __init__(self, rect =pygame.Rect(0,0,10,10) , text="", font=pygame.font.Font(None, 24), color=white, hover_color=white, action=None, border_color=black, border_width=0, surface = None, actionParameters=None,textColor=white):
        self.rect = rect
        self.actionParameters = actionParameters
        self.border_color = border_color
        self.surface1 = surface
        self.border_width = border_width
        self.text = font.render(text, True, textColor)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.surface = pygame.Surface((rect.width,rect.height), pygame.SRCALPHA)
        self.posRect = pygame.Rect(rect.width/2,rect.height/2,rect.width,rect.height)
        self.dimRect = pygame.Rect(0,0,rect.width,rect.height)
        try:
            self.surface.set_alpha(color[4])
        except IndexError:
            self.surface.set_alpha(255)
    def run(self):
        self.draw()
        self.surface1.blit(self.surface,(self.rect.x,self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            # if self.hovered:
            #     print("Hobered")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and self.action:
                if self.actionParameters:
                    self.action(*self.actionParameters)
                else:
                    self.action()
    def draw(self):
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(self.surface, color, self.dimRect)
        if self.border_width != 0:
            pygame.draw.rect(self.surface, self.border_color, self.dimRect, self.border_width)
        text_rect = self.text.get_rect(center=self.dimRect.center)
        self.surface.blit(self.text, text_rect)
# button = Button(rect=pygame.Rect(0, 0, 100, 100), text="Meow",color=(100,0,0,0), action=lambda: print("Button clicked!"), surface = screen, border_width=1)
# while True:
#     screen.fill(white)
#     button.run()
#     checkQuit(button.handle_event)
#     pygame.display.flip()
