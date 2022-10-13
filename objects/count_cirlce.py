from skimage.measure import regionprops
import matplotlib.pyplot as plt
import numpy  as np
from skimage.measure import label

data = np.load('objects/ellipses.npy')
data_labeled = label(data)
props = regionprops(data_labeled)
sum = 0
for i in range(0, data_labeled.max()):
    sum += (props[i]['eccentricity'] > 0)
print(sum)
#plt.imshow(data[props[2].])

plt.show()
