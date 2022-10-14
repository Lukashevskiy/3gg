import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import *
from matplotlib import use
from skimage.measure import label
use('Qt5Agg')
data = np.load('./count_objects/ps.npy').astype('uint8')
data_labeled = label(data)
data_erosied = binary_erosion(data, np.array([[1,1,1],[0,1,0],[1,1,1]]))
data_erosied_labeled = label(data_erosied)
#plt.figure()
f = open('output.txt', 'w')
print(f'number of figures on image: {data_labeled.max()}', file=f)
print(f'number of rectangles on image: {data_erosied_labeled.max()}', file=f)
print(f'number of other objects on image: {data_labeled.max() - data_erosied_labeled.max()}', file=f)

# plt.subplot(211)
# plt.imshow(data)
# plt.subplot(212)
# plt.imshow(data_erosied)
# plt.show()

