import numpy as np
import matplotlib.pyplot as plt
import cv2

# reading image
im = cv2.imread('resmim.jpg')
cv2.imshow('resmim.jpg',im)
cv2.waitKey(0)
# Calculate average value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# Histogram calculation
counts, bins = np.histogram(vals, range(257))
# Graph histogram focusing on the values ​​0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()

