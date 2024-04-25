from PIL import Image
import numpy as np

# Load the image
image = Image.open('resources/cat.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Now you can work with the image as a NumPy array
print(image_array.shape)  # This will print the shape of the array, e.g., (height, width, channels)
