import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.ndimage.morphology import *
from skimage.measure import label


matplotlib.use("Qt5Agg")
mask = np.ones((2,2))
#mask[:, 2] = 1
#mask[2, :] = 1
print(mask)
n = np.load('starsnpy')
print(f'count all objects: {label(n).max()}')
erosioned_image = binary_erosion(n,mask)
print(f'count rectangle: {label(erosioned_image).max()}' )
#plt.imshow(n[360:380, 300:310])
plt.imshow(n[146:156, 119:126])
plt.show()