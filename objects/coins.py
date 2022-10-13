import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.filters.thresholding import threshold_otsu, threshold_local, threshold_li, threshold_yen
from skimage.filters import gaussian  
from skimage.exposure import histogram

from matplotlib import use
use('Qt5Agg')

image = plt.imread('./objects/coins.jpg')
image_grey = np.mean(image, 2).astype('uint8')
# hist = histogram(image_grey)
# # plt.figure(1)
# # plt.subplot('121')
# # plt.imshow(image_grey, cmap='Greys')
# # plt.subplot('112')
# # plt.show()
# binary = image_grey.copy()
# binary[binary < 120] = 0
# binary[binary >= 120] = 1
# plt.imshow(binary)
#plt.plot(hist[1], hist[0])
#plt.show()
# def area(label: int, image: NDArray[Shape["2, 2"]]) -> int:
#     return (image == label).sum()

# data = np.load('./objects/coins.npy')

# data_labeled = label(data)

# area_coins = []

# for i in range(1, data_labeled.max()+1):
#     area_coins.append(area(i, data_labeled))

# all = 0
# dic = Counter(area_coins)
# for nominal, coins in zip([10,5,2,1], dic.values()):
#     all += (nominal * coins)

# print(Counter(area_coins))
# print(all)


image_1 = image_grey.copy() > threshold_local(image_grey, 101)
image_2 = image_grey.copy() > threshold_otsu(image_grey)
image_3 = image_grey.copy() > threshold_li(image_grey)
image_4 = image_grey.copy() > threshold_yen(image_grey)
plt.subplot(321)
plt.title('local')
plt.imshow(image_1)
plt.subplot(322)
plt.title('otsu')
plt.imshow(image_2)
plt.subplot(325)
plt.title('gaus')
plt.imshow(image_grey / gaussian(image_grey, 600))
plt.subplot(323)
plt.title('li')
plt.imshow(image_3)
plt.subplot(324)
plt.title('yen')
plt.imshow(image_4)
plt.show()
