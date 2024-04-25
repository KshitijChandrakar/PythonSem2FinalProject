from MyFunctions import *
import pygame, random, sys, os
from Filenames import *
vector = pygame.math.Vector2
coll = checkCollisionVector
class Box:
    # screenface = pygame.screenface((0,0))
    def changeVel(self, i):
        # print("Hi from changing velocity")
        self.Attributes["Velocity"][i] = map1(self.environmentAttributes["score"], 0, self.environmentAttributes["MaxScore"], self.Attributes["VelocityConstraints"][i][0], self.Attributes["VelocityConstraints"][i][1])
        # print(self.Attributes["Velocity"])
    def run(self):
        try:
            if self.Attributes["Update"]:
                self.update()
        except KeyError:
            pass
        try:
            if self.Attributes["Render"]:
                self.render()
        except KeyError:
            pass
        try:
            if self.Attributes["IncVelocity"][0]:
                self.changeVel(0)
            if self.Attributes["IncVelocity"][1]:
                self.changeVel(1)
        except KeyError:
            pass
        try:
            if self.Attributes["Collider"]:
                if self.checkCollision(removeNoneItem(self.environmentAttributes["Objects"], self)):
                    self.onCollision(self)
                    pass
                pass
            pass
        except KeyError:
            pass
        try:
            if self.Attributes["rest"] != None:
                # self.Attributes["Constrain"] = self.Attributes["Constrain"]
                for i in range(len(self.Attributes["pos"])):
                    if self.Attributes["Constrain"][i]:
                        # self.constrained = self.Attributes["Constrain1"][i] <= self.Attributes["pos"][i] - self.Attributes["Dimensions"][i]/2 < self.Attributes["pos"][i] + self.Attributes["Dimensions"][i]/2 <= self.Attributes["Constrain2"][i]
                        # print(f"{self.constrained} {self.Attributes['id']}")
                        try:
                            if self.Attributes["RevA"] == 0:
                                self.constrained = self.Attributes["Constrain1"][i] < self.Attributes["pos"][i] < self.Attributes["Constrain2"][i]
                            else:
                                self.constrained = self.Attributes["Constrain1"][i] < self.Attributes["pos"][i] - self.Attributes["Dimensions"][i]/2 < self.Attributes["pos"][i] + self.Attributes["Dimensions"][i]/2 < self.Attributes["Constrain2"][i]
                        except KeyError:
                            self.constrained = self.Attributes["Constrain1"][i] < self.Attributes["pos"][i] - self.Attributes["Dimensions"][i]/2 < self.Attributes["pos"][i] + self.Attributes["Dimensions"][i]/2 < self.Attributes["Constrain2"][i]

                    else:
                        self.constrained = 1
                    if not self.constrained:
                        try:
                            if not self.Attributes["RevA"]:
                                self.Attributes["Velocity"][i], self.Attributes["Acceleration"][i] = self.Attributes["DefaultVelocity"][i], self.Attributes["DefaultAcceleration"][i]
                                pass
                        except KeyError:
                            self.Attributes["Velocity"][i], self.Attributes["Acceleration"][i] = self.Attributes["DefaultVelocity"][i], self.Attributes["DefaultAcceleration"][i]

                        # If it goes out of constrains then check if randomise is true if it is
                        # then randomie the position from randomisationList else go to rest position
                        # and reset velocity and Acceleration
                        #Applying Constrains
                        #Randomise Position
                        if self.Attributes["randomise"][i] == 1 and self.Attributes["randomisationList"][i]:
                            self.Attributes["pos"][i] = self.randomScalar(i)
                        elif self.Attributes["randomise"][i] == 0:
                            try:
                                self.Attributes["Velocity"][i] *= self.Attributes["Rev"]
                            except KeyError:
                                # print(f'resetting {self.Attributes['id']}')
                                self.debug()

                                self.Attributes["pos"][i] = self.Attributes["rest"][i]
                    elif self.constrained and not self.Attributes["Anti-Gravity"]:
                        #Applying Gravity
                        self.Force(self.environmentAttributes["Gravity"])
        except KeyError:
            raise
    def randomScalar(self, i):
        # print(i)

        return random.randrange(int(self.Attributes["randomisationConstrain"][i][0]), int(self.Attributes["randomisationConstrain"][i][1]))
    def randomVector(self):
        return vector(self.randomScalar(0), self.randomScalar(1))
    def randomise(self, what):
        for i in range(len(what)):
            try:
                if self.Attributes["randomisationList"][i]:
                    what[i] = self.randomScalar(i)
            except IndexError:
                continue
    def render(self):
        try:
            if self.Attributes["Sprites"]:
                try:
                    try:
                        CurrentFrameNumber = int((self.environmentAttributes['score']//self.Attributes["changeFrameCount"][self.Attributes["CurrentSprite"]])%len(self.sprites[self.Attributes["CurrentSprite"]]))
                    except KeyError:
                        CurrentFrameNumber = int((self.environmentAttributes['score']//self.Attributes["changeFrameCount"])%self.spritesheet[0].cols)
                except ZeroDivisionError:
                    CurrentFrameNumber = 0
                # self.environmentAttributes["screen"].blit(self.sprites[CurrentFrameNumber], self.Attributes["pos"])
                try:
                    if self.Attributes["SwitchSprites"]:
                        self.environmentAttributes["screen"].blit(pygame.transform.scale(self.sprites[self.Attributes["CurrentSprite"]][CurrentFrameNumber].convert_alpha(), self.Attributes["Dimensions"]), self.Attributes["pos"])
                    else:
                        self.environmentAttributes["screen"].blit(pygame.transform.scale(self.sprites[CurrentFrameNumber].convert_alpha(), self.Attributes["Dimensions"]), self.Attributes["pos"])
                except KeyError:
                    self.environmentAttributes["screen"].blit(pygame.transform.scale(self.sprites[CurrentFrameNumber].convert_alpha(), self.Attributes["Dimensions"]), self.Attributes["pos"])
        except (KeyError, IndexError):
            try:
                if self.Attributes["Image"]:
                    image = []
                    for i in self.Attributes['Image']:
                        image.append(pygame.transform.scale(pygame.image.load(i).convert_alpha(), self.Attributes["Dimensions"]))

                    # self.environmentAttributes["score"]
                    NumOfImages = len(image)
                    try:
                        CurrentFrameNumber = int((self.environmentAttributes['score']//self.Attributes["changeFrameCount"])%NumOfImages)
                    except ZeroDivisionError:
                        CurrentFrameNumber = 0
                    self.environmentAttributes["screen"].blit(image[CurrentFrameNumber], self.Attributes["pos"])
            except (KeyError, IndexError):
                pygame.draw.rect(self.environmentAttributes["screen"], self.Attributes["color"], (self.Attributes["pos"].x, self.Attributes["pos"].y, self.Attributes["Dimensions"].x, self.Attributes["Dimensions"].y))
                pass
        # self.environmentAttributes["screen"].fill((255,0,0))
        pass
    def update(self):
        self.Attributes["Velocity"] += self.Attributes["Acceleration"]
        self.Attributes["pos"] += self.Attributes["Velocity"]
        self.Attributes["Acceleration"] = vector(0,0)




        # self.Attributes["Acceleration"] = vector(0,0)
    def checkCollision(self, ObjList):
        try:
            if self.Attributes["Collider"]:
                for object in ObjList:
                    if object != None:
                        if coll(self.Attributes["pos"],self.Attributes["Dimensions"], object.Attributes["pos"], object.Attributes["Dimensions"]):
                            return True
                return False
            else:
                return False
        except KeyError:
            return False
        pass
    def Force(self, F):
        self.Attributes["Acceleration"] += F
        # self.Attributes["pos"].x
        pass
    def Force1(self, F, i):
        self.Attributes["Acceleration"][i] += F[i]
        # self.Attributes["pos"].x
        pass
    def debug(self):
        # print("\033[0;0H")
        try:
            if self.Attributes["Debug"]:
                print(self.Attributes["id"], self.Attributes["Velocity"], )
        except KeyError:
            pass
    def __init__(self, Attr, env):
        # print()
        # print("initializing...", Attr["id"], Attr["Default"])
        self. Attributes = Attr
        self.environmentAttributes = env
        self.Attributes["pos"] = vector(-1,-1)
        self.Attributes["pos"] = self.Attributes["Default"].copy()# if not self.Attributes["randomise"] else self.randomise(self.Attributes["pos"])
        self.Attributes["Velocity"] = self.Attributes["DefaultVelocity"].copy()
        self.Attributes["Acceleration"] = self.Attributes["DefaultAcceleration"].copy()
        try:
            self.onCollision = self.Attributes["CollisionFunction"] if self.Attributes["Collider"] else EmptyFunction
        except KeyError:
            pass
        try:
            if self.Attributes["SwitchSprites"] == False:
                self.spritesheet = self.Attributes["Sprites"]
                self.sprites = self.Attributes["Sprites"].load_grid_images(self.Attributes["RowAndColumn"][0], self.Attributes["RowAndColumn"][1], x_padding= self.Attributes["Padding"][0], y_padding= self.Attributes["Padding"][1], x_margin= self.Attributes["Margin"][0], y_margin= self.Attributes["Margin"][1])
            else:
                self.sprites = []
                for i in range(len(self.Attributes["Sprites"])):
                    # self.spritesheet.append(self.Attributes["Sprites"][i])
                    self.sprites.append(self.Attributes["Sprites"][i].load_grid_images(self.Attributes["RowAndColumn"][i][0], self.Attributes["RowAndColumn"][i][1], x_padding= self.Attributes["Padding"][i][0], y_padding= self.Attributes["Padding"][i][1], x_margin= self.Attributes["Margin"][i][0], y_margin= self.Attributes["Margin"][i][1]))

        except KeyError:
            pass
        # print("initialized...", self.Attributes["id"], self.Attributes["Default"])
        pass
# x = Box(playerAttributes)
