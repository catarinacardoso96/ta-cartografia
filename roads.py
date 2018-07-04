import cv2
import numpy as np

#-----Function that computes color distance---------------------------------
def dist2gray(R,G,B):
    R1 = 180
    G1 = 180
    B1 = 180
    return np.sqrt(pow(R - R1, 2) + pow(G - G1, 2) + pow(B - B1, 2))

#-----Reading the image-----------------------------------------------------
img = cv2.imread('test.png', 1)

#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
#-----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl,a,b))
#-----Converting image from LAB Color model to RGB model--------------------
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

#-----Matrix of grayscale distances-----------------------------------------
graydists = np.zeros((final.shape[0], final.shape[1]))

for i in range(graydists.shape[0]):
    for j in range(graydists.shape[1]):
        graydists[i,j] = dist2gray(final[i,j,2], final[i,j,1], final[i,j,0])

#-----Binarize and dilate result--------------------------------------------
a, b = cv2.threshold(graydists,250,255,cv2.THRESH_TRUNC)
c, d = cv2.threshold(b,120,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.dilate(d,kernel,iterations = 1)

#-----Paint streets yellows-------------------------------------------------
img_b = img[:,:,0]
img_g = img[:,:,1]
img_r = img[:,:,2]

img_b[erosion != 255] = 175
img_g[erosion != 255] = 242
img_r[erosion != 255] = 255

img[:,:,0] = img_b
img[:,:,1] = img_g
img[:,:,2] = img_r

#-----Save results----------------------------------------------------------
cv2.imwrite('result.png', img)