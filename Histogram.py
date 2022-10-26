import numpy as np
import matplotlib.pyplot as plt
import cv2

# resim okuma
im = cv2.imread('resmim.jpg')
cv2.imshow('resmim.jpg',im)
cv2.waitKey(0)
# RGB kanallarından ortalama değeri hesaplayın ve 1D dizisine düzleştirin
vals = im.mean(axis=2).flatten()
# Histogram hesaplama
counts, bins = np.histogram(vals, range(257))
# 0..255 değerlerine odaklanan grafik histogramı
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()

