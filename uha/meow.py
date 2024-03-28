import matplotlib.pyplot as plt
import pickle
from matplotlib.collections import LineCollection

import numpy as np
# from movenet import _keypoints_and_edges_for_display
with open('Tensorflow testing/keypoints.pkl', 'rb') as file:
    keypoints = pickle.load(file)
with open('Tensorflow testing/output_overlay.pkl', 'rb') as file:
    output_overlay = pickle.load(file)
with open('Tensorflow testing/display_image.pkl', 'rb') as file:
    display_image = pickle.load(file) # (1,1280,1280,3)
with open('Tensorflow testing/input_image1.pkl', 'rb') as file:
    image = pickle.load(file)
with open('Tensorflow testing/input_image.pkl', 'rb') as file:
    input_image = pickle.load(file)
with open('Tensorflow testing/keypoint_coords.pkl', 'rb') as file:
    keypoint_coords = pickle.load(file)
with open('Tensorflow testing/keypoint_locs.pkl', 'rb') as file:
    keypoint_locs = pickle.load(file)
with open('Tensorflow testing/keypoint_edges.pkl', 'rb') as file:
    keypoint_edges = pickle.load(file)
with open('Tensorflow testing/edge_colors.pkl', 'rb') as file:
    edge_colors = pickle.load(file)
x_coords = [point[0] for point in keypoint_locs]
y_coords = [point[1] for point in keypoint_locs]
plt.scatter(x_coords, y_coords)
plt.imshow(np.squeeze(display_image, axis=0))
plt.show()
