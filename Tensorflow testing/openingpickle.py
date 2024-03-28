import pickle
with open('Tensorflow testing/keypoints.pkl', 'rb') as file:
    _ = pickle.load(file)
print(_)
