from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import use

use("Qt5Agg")

def area(image, label):
    return (image == label).sum()
 
 
def centroid(image, label):
    pos = np.where(image == label)
    cy = np.mean(pos[0])
    cx = np.mean(pos[1])
    return cy, cx
 
 
def neighbors4(y, x):
    return (y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x)
 
 
def neighborsX(y, x):
    return (y - 1, x + 1), (y + 1, x - 1), (y + 1, x + 1), (y - 1, x - 1)
 
 
def neighbors8(y, x):
    return neighbors4(y, x) + neighborsX(y, x)
 
 
def boundaries(image, label=1, connectivity=neighbors4):
    bounds = []
    pos = np.where(image == label)
    for y, x in zip(*pos):
        for yn, xn in connectivity(y, x):
            if yn < 0 or yn > image.shape[0] - 1:
                bounds.append((y, x))
            elif xn < 0 or xn > image.shape[1] - 1:
                bounds.append((y, x))
            elif image[yn, xn] != label:
                bounds.append((y, x))
    return bounds
 
 
def perimeter(image, label=1, connectivity=neighbors4):
    return len(boundaries(image, label, connectivity))
 
 
def distance(px1, px2):
    return ((px1[0] - px2[0]) ** 2 + ((px1[1] - px2[1]) ** 2)) ** 0.5
 
 
def radial_distance(image, label, connectivity):
    r, c = centroid(image, label)
    bounds = boundaries(image, label, connectivity)
    K = len(bounds)
    rd = 0
    for rk, ck in bounds:
        rd += distance((r, c), (rk, ck))
    return rd / K
 
 
def std_radial(image, label, connectivity):
    r, c = centroid(image, label)
    bounds = boundaries(image, label, connectivity)
    K = len(bounds)
    sr = 0
    rd = radial_distance(image, label, connectivity)
    for rk, ck in bounds:
        sr += (distance((r, c), (rk, ck)) - rd) ** 2
    return (sr / K) ** 0.5
 
 
def circularity_std(image, label=1, connectivity=neighbors4):
    return (radial_distance(image, label, connectivity)) / std_radial(image, label, connectivity)
 
 

 
results = {}
 

 
image = np.zeros((16, 16))
image[4:, :4] = 2
 
image[3:10, 8:] = 1
image[[3, 4, 3], [8, 8, 9]] = 0
image[[8, 9, 9], [8, 8, 9]] = 0
image[[3, 4, 3], [-2, -1, -1]] = 0
image[[9, 8, 9], [-2, -1, -1]] = 0
 
image[12:-1, 6:9] = 3
 
image = label(image)
mx = np.max(image)
 
for i in range(1, mx + 1):
    print(circularity_std(image, i))
 
plt.imshow(image)
plt.show()
 
