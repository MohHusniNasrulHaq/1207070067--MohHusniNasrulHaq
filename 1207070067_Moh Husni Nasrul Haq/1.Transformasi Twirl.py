#mengimport library yang digunakan
import matplotlib.pyplot as plt 
import cv2

from skimage import data 
from skimage.transform import swirl 
#memanggil gambar yang disimpan dengan opencv
image = cv2.imread('hitamputih.jpg') 

#melakukan operasi swirl dengan ketentuan nilai-nilai dari rotasi,strength, dan juga radius
swirled = swirl(image, rotation=0, strength=10, radius=300) 

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, 
figsize=(8, 3), sharex=True, sharey=True) 

ax0.imshow(image, cmap=plt.cm.gray) 
ax0.axis('off') 
ax1.imshow(swirled, cmap=plt.cm.gray) 
ax1.axis('off') 
plt.show() 