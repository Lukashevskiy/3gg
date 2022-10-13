import re
import numpy as np
import matplotlib.pyplot as plt
from pyrsistent import ny
from scipy.misc import face
from scipy.ndimage.morphology import *
from skimage.measure import label

import os


arr = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]])

def translation(image, vector):
    translated = np.zeros_like(image)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            ny = y + vector[0]
            nx = x + vector[1]
# plt.subplot(121)
# plt.imshow(arr)
# plt.subplot(122)
# plt.imshow(arr_c)

# plt.show()

            # ny %= (image.shape[0]-1)
            # nx %= (image.shape[1]-1)
            # without zeros
            # if ny < 0 or nx < 0:
            #     nx %= image.shape[0]
            # if ny >= image.shape[0] or nx >= image.shape[1]:
            #     continue
            # with zeros

            translated[ny, nx] = image[y, x] 
    return translated
#arr = face(True)
#arr_c = translation(arr, (50, -50))
struct = np.ones((3,3))
#struct = np.array([[1, 0, 1],
#                [0, 1, 0],
#                [1, 0, 1],])
# def dilation(arr, mask):
#     result = np.zeros_like(arr)
#     for y in range(1, arr.shape[0]-1):
#         for x in range(1, arr.shape[1]-1):
#             rlog = np.logical_xor(arr[y, x], mask)
#             result[y-1:y+2, x-1: x+2] = np.logical_or(result[y-1:y+2, x-1:x+2], rlog)
#     return result

# def erosion(arr, mask):
#     result = np.zeros_like(arr)
#     for y in range(1, arr.shape[0]-1):
#         for x in range(1, arr.shape[1]-1):
#             sub = arr[y-1:y+2, x-1:x+2]
#             pos = mask > 0
#             if np.all(sub[pos] == mask[pos]):
#                 result[y, x] = 1

#     return result

def closing(arr, mask):
    result = binary_erosion(arr, mask)
    return binary_dilation(result, mask)


def open(arr, mask):
    result = binary_dilation(arr, mask)
    return binary_erosion(result, mask)


#arr_c = np.load('./wires2.npy')
#print(arr_c)
# plt.figure(1)
# plt.subplot(121)
# plt.imshow(arr)
# plt.subplot(122)
# plt.imshow(arr_c)

# plt.show()
data_paths = []
for file in os.listdir():
    if file.find('npy') != -1:
        data_paths.append(file)

#file = data_paths[j]
for index, file in enumerate(data_paths[:]):
    print(f"{index}) file name - {file}")
    image = np.load(file)
    labeled_image = label(image)
    print(f'count wires - {labeled_image.max()}')
    for i in range(1, labeled_image.max()+1):
        current_image_of_wire = np.zeros_like(labeled_image)
        current_image_of_wire[labeled_image == i] = 1
       
        current_image_of_wire = binary_erosion(current_image_of_wire, np.array([[0,1,0],[0,1,0],[0,1,0]]))
       
        
        print(f'\twires - {i}')
        
        parts = label(current_image_of_wire).max()
        print(f'\tconsist of -{ parts }')
