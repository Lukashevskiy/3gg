import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import *
from matplotlib import use
from skimage.measure import label
use('Qt5Agg')

data = np.load('ps.npy').astype('uint8')
data_labeled = label(data)
print(f'number of figures on image: {data_labeled.max()}')
data_erosied = binary_erosion(data)
plt.figure()
plt.imshow(data_erosied)
plt.show()
