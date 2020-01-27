# scipy.test.py
import imageio
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Read an JPEG image into a numpy array
img = imageio.imread('assets/cat.jpg')
print(img.dtype, img.shape)

img_tinted = img * [1, 0.95, 0.9]
# imageio.imsave('assets/cat_tinted.jpg', img_tinted)

x = np.array([[0,1],[1,0],[2,0]])
print(x)

d = squareform(pdist(x, 'euclidean'))
print(d)