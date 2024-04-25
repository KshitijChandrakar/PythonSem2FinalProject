# Final Project for semester 2 python
Name: Kshitij Chandrakar  
Course: B.Tech CSE (Hons)  
Semester: 2   
SAP: 500124827   
Enrollment Number: 2142231661  

Topic: Video Game Using Computer Vision

### About the project:
As the name suggest, its a platform based runner game, however the controls are based on the movement of the user as captured by the camera.  
it utilizes various technologies like:
 - Movenet
 - Tensorflow
 - Computer Vision

in the game You can jump, dodge obstacles and the character follows your actual body movements as captured from the camera

# To do List

 1. Create The Base Game
      - [x] Its a game where you have to dodge obstacles
      - [x] Create the Sprites
      - Create the body models
 2. [x] Train an AI model to recognise body movement
      - [x] Preferably use Google's  teachable machine otherwise we could do tensorflow from scratch (Although that would create a problem with the dataset but whatever)
      - [x] used movenet
 3. [x] Track average body postion relative to previous position to check if it jumped
    - if it did jump then jump the main character
    - Added Controls for the character
 4. If possible, add body models to the game along with animations that follow the body movement

---
**Explanation For the Main GameLoop System**:

 ### 1. Imports:
 ```python
 from MyColors import *
 from MyFunctions import *
 import random, os
 from ObjectClass import *
 from buttons import *
 from scene import *
 from Attributes import *
 ```
 - These lines import various modules needed for the game:
   - `MyColors`: Likely contains predefined color constants.
   - `MyFunctions`: Probably contains custom functions for the game.
   - `random`: Python's built-in module for generating random numbers.
   - `os`: Python's built-in module for interacting with the operating system.
   - `ObjectClass`: Contains the definition of the `Box` class for game objects.
   - `buttons`: Provides functionality for creating buttons in the game interface.
   - `scene`: Handles scene management in the game.
   - `Attributes`: Holds attributes and configurations for the game.

 ### 2. Initialization and Environment Setup:
 ```python
 print("RAAAAAAAAAAAAAH IM STARTING UP RAWr")
 clock = pygame.time.Clock()
 movenetUsed = 0
 ```
 - The program prints a startup message.
 - `pygame.time.Clock()` creates a clock object to control the game's frame rate.
 - `movenetUsed` is set to 0, indicating that a motion control system (possibly for player movement) is not being used.

 ### 3. High Score Management:
 ```python
 def setHighScore():
     with open(highScoreFile, 'w') as file:
         file.write(str(environmentAttributes["highScore"]))
 ```
 - This function writes the current high score to a file.

 ### 4. Environment Setup:
 ```python
 font = pygame.font.Font(r"Gotham-Bold.otf", 32)
 # Additional font objects with different sizes
 ```
 - Fonts are loaded for rendering text with different sizes.

 ```python
 def resetEnv():
     # Code to reset the game environment, including player and obstacles.
     pass
 ```
 - This function resets the game environment, initializing player and obstacle objects.

 ```python
 script_dir = os.path.dirname(os.path.abspath(__file__))
 highScoreFile = os.path.join(script_dir, 'highScore.txt')
 # Read from the input file
 with open(highScoreFile, 'r') as file:
     environmentAttributes["highScore"] = int(float(file.read()))
 ```
 - It reads the high score from a file and initializes it in the game environment attributes.

 ### 5. Event Handling and Game Logic:
 ```python
 def updateEnv():
     # Function to update the game environment based on the current score.
     pass
 ```
 - This function updates the game environment based on the current score, possibly adjusting difficulty.

 ```python
 def checkEvent(event):
     # Function to handle user input events such as keyboard input.
     pass
 ```
 - It handles user input events such as keyboard presses, controlling player actions.

 ```python
 def centerText(centerTextStr, x_offset = 0, y_offset=0, color=white, font=font):
     # Function to render centered text on the screen.
     pass
 ```
 - This function renders text centered on the screen with optional offsets, color, and font.

 ### 6. Rendering and Screen Management:
 ```python
 def StartScreen():
     # Function to render the start screen.
     pass
 ```
 - It renders the start screen of the game.

 ```python
 def GameLoop():
     # Main game loop function, responsible for running the game logic.
     pass
 ```
 - This function represents the main game loop, executing game logic and rendering frames.

 ### 7. Scene Management:
 ```python
 currentScene  = "StartScreen"
 scenes = {}
 ```
 - `currentScene` stores the current scene name.
 - `scenes` is a dictionary that maps scene names to their respective functions and attributes.

 ```python
 def changeScene(a):
     # Function to change the current scene.
     pass
 ```
 - This function changes the current scene to the one specified.

 ### 8. Main Loop:
 ```python
 while True:
     # Main game loop where events are processed, scenes are rendered, and game logic is executed.
     pass
 ```
 - The program enters a perpetual loop where events are handled, scenes are rendered, and game logic is executed continuously.
---
```Python

```
The ObjectClass code defines a class `Box` which seems to represent a game object or entity.
1. **Attributes and Initialization**:
  ```Python
      from MyFunctions import *
      import pygame, random, sys, os
      from Filenames import *
      vector = pygame.math.Vector2
      coll = checkCollisionVector
  ```
   - The class has various attributes like position, velocity, acceleration, etc., which are initialized in the `__init__` method.
   - Attributes are accessed using a dictionary (`self.Attributes`), where keys are strings representing attribute names.

2. **Rendering**:

  ```Python
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
  ```
 - The `render` method seems to handle rendering of the object on the screen. It supports rendering with sprites, images, or simple rectangles.
   - It utilizes Pygame for rendering and scaling images/sprites.

3. **Updating**:

  ```Python
  def update(self):
      self.Attributes["Velocity"] += self.Attributes["Acceleration"]
      self.Attributes["pos"] += self.Attributes["Velocity"]
      self.Attributes["Acceleration"] = vector(0,0)

  ```
   - The `update` method updates the position of the object based on its velocity and acceleration.
   - Acceleration is applied to velocity, and velocity is applied to position.

4. **Collision Detection**:
  ```Python
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
  ```
   - The `checkCollision` method seems to check for collisions between this object and others passed as a list.
   - It uses a function `checkCollisionVector` imported from `MyFunctions`.

5. **Forces and Constraints**:
   - There are methods like `Force` and `Force1` for applying forces to the object.
   - Constraints are applied to restrict the object's movement within specified bounds.

6. **Other Functionalities**:
   - There are methods for handling randomization of position and vectors (`randomScalar`, `randomVector`, `randomise`).
   - Debugging functionality (`debug`) is available to print debug information if enabled.

7. **Main Loop**:
   - The `run` method seems to orchestrate the main operations of the object, including update, render, collision detection, and constraint enforcement.
---
Certainly! Let's break down each method and provide detailed explanations along with the corresponding code snippets:

```python
from MyFunctions import EmptyFunction
'''
Scene is a subset of Environment
'''
class Scene:
    def handleExp(self, E):
        # Method to handle exceptions raised by the scene
        try:
            self.excep[E][0](self.excep[E][1])
        except (KeyError, TypeError):
            pass

    def initialise(self):
        # Method to initialize the scene
        try:
            for i in self.initialise1:
                i()
        except TypeError:
            pass

    def uninitialise(self):
        # Method to uninitialize the scene
        try:
            for i in self.uninitialise1:
                i()
        except TypeError:
            pass

    def __init__(self, renderFunction, event=None, excep=None, eventFunction=None, initialise=None, uninitialise=None):
        # Constructor method to initialize the Scene object
        self.initialise1 = initialise
        self.Initialised = 0
        self.uninitialise1 = uninitialise
        self.renderFunction = renderFunction
        self.events = event  # Events = {eventType: what To do in case of event}
        self.excep = excep  # Exceptions that scenes raise
        self.eventFunction = eventFunction  # A function to call with event as the parameter

    def render(self):
        # Method to render the scene
        self.renderFunction()

    def handleEvent(self, event):
        # Method to handle events
        try:
            self.events[event][0](self.events[event][1])
        except IndexError:
            self.events[event][0]()
        except KeyError:
            pass
```
**Explanation For the Scene System**:

1. **handleExp(self, E)**:
   - This method handles exceptions raised by the scene.
   - It attempts to execute the exception handling function corresponding to the provided exception `E`.

2. **initialise(self)**:
   - This method initializes the scene.
   - It iterates over a list of initialization functions (`initialise1`) and executes each function.

3. **uninitialise(self)**:
   - This method uninitializes the scene.
   - It iterates over a list of uninitialization functions (`uninitialise1`) and executes each function.

4. **__init__(self, renderFunction, event=None, excep=None, eventFunction=None, initialise=None, uninitialise=None)**:
   - This is the constructor method for the `Scene` class.
   - It initializes the scene with the provided parameters:
     - `renderFunction`: Function to render the scene.
     - `event`: Dictionary containing event types and corresponding actions.
     - `excep`: Dictionary containing exception types and corresponding exception handling functions.
     - `eventFunction`: Function to handle events.
     - `initialise`: List of functions to initialize the scene.
     - `uninitialise`: List of functions to uninitialize the scene.

5. **render(self)**:
   - This method renders the scene by calling the provided render function (`renderFunction`).

6. **handleEvent(self, event)**:
   - This method handles events received by the scene.
   - It attempts to execute the corresponding event handling function based on the event type.
---
**Explanation For the SpriteSheet System**:

```python
from pygameInit import *
from pygame.math import Vector2 as vector
from MyColors import *
from MyFunctions import *
import os
```
- **Imports**:
  - The code imports necessary modules including custom ones (`pygameInit`, `MyColors`, `MyFunctions`) and standard ones (`os`, `pygame.math`).
  - It initializes Pygame with `pygameInit`.

```python
width, height = startPygame(hypo = 1000, ratioa = 21, ratiob = 10, caption = "AAAAAAAAA")
screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)
```
- **Pygame Initialization**:
  - It initializes Pygame with specific parameters such as window size (`width`, `height`) and window caption.

```python
class SpriteSheet:
    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
```
- **SpriteSheet Class Initialization**:
  - It defines a class `SpriteSheet` to handle sprite sheets.
  - The `__init__` method loads the sprite sheet image from the provided filename.

```python
    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)  # Create surface with per-pixel alpha
        image.blit(self.sheet, (0, 0), rect)

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
```
- **image_at Method**:
  - It extracts a specific image from a rectangle within the sprite sheet.
  - Optionally, it sets a colorkey for transparency if provided.

```python
    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]
```
- **images_at Method**:
  - It loads a list of images from a list of rectangles and returns them as a list.

```python
    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
```
- **load_strip Method**:
  - It loads a strip of images (e.g., animation frames) from a single rectangle and returns them as a list.

```python
    def load_grid_images(self, num_rows, num_cols, x_margin=0, x_padding=0,
            y_margin=0, y_padding=0):
        """Load a grid of images."""
        # Code snippet explaining the load_grid_images method
```
- **load_grid_images Method**:
  - It loads a grid of images from the sprite sheet, arranging them in rows and columns.
  - Parameters `x_margin`, `x_padding`, `y_margin`, `y_padding` control spacing between sprites.
---
**Explanation For the Movenet System**:

### Imports:
- **tensorflow and tensorflow_hub**: Importing TensorFlow and TensorFlow Hub for loading and running the MoveNet model.
- **tensorflow_docs.vis.embed**: Importing the `embed` function from `tensorflow_docs.vis` module for embedding visualizations.
- **numpy**: Importing NumPy for numerical computations.
- **cv2**: Importing OpenCV for image processing.
- **MovenetAttributes**: Importing custom attributes (`KEYPOINT_DICT`, `KEYPOINT_EDGE_INDS_TO_COLOR`) related to the MoveNet model.
- **matplotlib.pyplot**: Importing Matplotlib's pyplot module for visualization.
- **matplotlib.collections**: Importing LineCollection from matplotlib.collections for drawing lines.
- **matplotlib.patches**: Importing patches module from matplotlib for drawing shapes.
- **imageio and IPython.display**: Importing imageio for working with image sequences and IPython.display for displaying HTML content.

### Function Definitions:
1. **`extract_keypoint_coordinates`**: Extracts xy coordinates of keypoints from keypoints with scores array.
2. **`keypoints_and_edges_for_display`**: Returns high confidence keypoints and edges for visualization.
3. **`draw_prediction_on_image`**: Draws keypoint predictions on the image.
4. **`to_gif`**: Converts an image sequence (4D numpy array) to a GIF.
5. **`progress`**: Displays a progress bar as HTML.
6. **`movenet1`**: Runs detection on an input image using the MoveNet model.
7. **`init_crop_region`**: Defines the default crop region.
8. **`torso_visible`**: Checks whether there are enough torso keypoints for determining the crop region.
9. **`determine_torso_and_body_range`**: Calculates the maximum distance from each keypoint to the center location.
10. **`determine_crop_region`**: Determines the region to crop the image for the model to run inference on.
11. **`crop_and_resize`**: Crops and resizes the image to prepare for the model input.
12. **`run_inference`**: Runs model inference on the cropped region.
13. **`Outliers`**: Detects outliers in the given data using the z-score method.
---
# Conclusion:
the Above Code Summary Outlined how the game works.
