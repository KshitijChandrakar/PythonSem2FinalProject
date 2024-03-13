Final Project for my semester 2 python module
# What the game is about

You jump and the character follows you

# To do List

 1. Create The Base Game
      - Its a game where you have to dodge obstacles
 2. Train an AI model to recognise body movement
      - Preferably use Google's  teachable machine otherwise we could do tensorflow from scratch (Although that would create a problem with the dataset but whatever)
 3. Track average body postion relative to previous position to check if it jumped
    - if it did jump then jump the main character
 4. If possible, add body models to the game along with animations that follow the body movement 


# Main.py Documentation

## Imports
```python
from pygameInit import *
from myColors import *
from MyFunctions import *
import random, os
from ObjectClass import *
from scene import *
```
- Import necessary modules for the program.

## Initialization
```python
print("RAAAAAAAAAAAAAH IM STARTING UP RAWr")
```
- Print a startup message.

## Custom Exception
```python
class myException(Exception):
    def __init__(self, id):
        self.id = id
```
- Define a custom exception class `myException` with an identifier.

## Environment Attributes
```python
vector = pygame.math.Vector2
width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "Dino without AI")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
```
- Set up environment attributes such as screen dimensions and clock.

## Game Over Function
```python
def gameOverFunc(i):
    print("Game Over by Collision of", i.Attributes["id"])
    environmentAttributes["GameOver"] = True
    raise myException("GameOver")
```
- Define a function to handle game over events.

## High Score Function
```python
def setHighScore():
    with open(highScoreFile, 'w') as file:
        file.write(str(environmentAttributes["highScore"]))
```
- Define a function to set the high score.

## Environment Setup
```python
font = pygame.font.Font(r"Gotham-Bold.otf", 32)
```
- Set the font for rendering text.

```python
environmentAttributes = {...}
```
- Define attributes for the game environment such as gravity, screen dimensions, and score.

## Player and Obstacle Attributes
```python
playerAttributes = {...}
obstacleAttributes = {...}
```
- Define attributes for the player and obstacles.

## Environment Reset
```python
def resetEnv():
    ...
```
- Define a function to reset the environment.

## High Score File
```python
script_dir = os.path.dirname(os.path.abspath(__file__))
highScoreFile = os.path.join(script_dir, 'highScore.txt')
```
- Define the path for the high score file.

```python
with open(highScoreFile, 'r') as file:
    environmentAttributes["highScore"] = int(float(file.read()))
```
- Read the high score from the file.

## Environment Reset and Initialisation
```python
def resetEnv1():
    ...
```
- Define a function to reset the environment and set the high score.

```python
resetEnv()
```
- Reset the environment.

## Defining Functions
```python
def updateEnv():
    ...
```
- Define a function to update the environment.

```python
def checkEvent(event):
    ...
```
- Define a function to check events.

```python
def centerText(centerTextStr):
    ...
```
- Define a function to center text on the screen.

```python
def StartScreen():
    ...
```
- Define a function for the start screen.

```python
def GameLoop():
    ...
```
- Define the main game loop function.

```python
def GameOver():
    ...
```
- Define a function for the game over screen.

```python
def Won():
    ...
```
- Define a function for the win screen.

## Scene Management
```python
scenes = {...}
```
- Define scenes for managing different parts of the game.

```python
currentScene  = "StartScreen"
```
- Set the current scene to the start screen.

```python
def changeScene(a):
    ...
```
- Define a function to change scenes.

## Main Loop
```python
while True:
    ...
```
- Run the main game loop.
---

# GameObject.py Documentation
This Part details the the GameObject class
## Imports
```python
from MyFunctions import *
import pygame, random, sys
```
- Import necessary modules for the program.

## Box Class
```python
class Box:
    def __init__(self, Attr, env):
        ...
```
- Define the Box class for game objects.

### Attributes:
- `Attributes`: Dictionary containing attributes of the box.
- `environmentAttributes`: Dictionary containing environment attributes.

### Methods:
#### Initialization:
- `__init__(self, Attr, env)`: Initialize the Box object with given attributes and environment.

#### Main Functions:
- `run(self)`: Run the Box object.
- `update(self)`: Update the position and velocity of the Box object.
- `render(self)`: Render the Box object on the screen.

#### Collision Handling:
- `checkCollision(self, ObjList)`: Check collision between the Box object and a list of other objects.
- `onCollision(self)`: Define action to be taken upon collision.

#### Forces and Acceleration:
- `Force(self, F)`: Apply force to the Box object.
- `Force1(self, F, i)`: Apply force in a specific direction to the Box object.

#### Miscellaneous:
- `debug(self)`: Print debug information about the Box object.

#### Helper Functions:
- `changeVel(self, i)`: Change the velocity of the Box object.
- `randomScalar(self, i)`: Generate a random scalar value.
- `randomVector(self)`: Generate a random vector.
- `randomise(self, what)`: Randomize specific attributes of the Box object.

## Helper Functions
```python
vector = pygame.math.Vector2
coll = checkCollisionVector
```
- Define helper functions and variables.
