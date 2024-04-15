import numpy as np
import matplotlib.pyplot as plt

img_array = plt.imread('avatar cool.jpg')
print(img_array)
x = img_array/255
plt.figure(figsize=(10,10))
plt.imshow(x)
plt.show()