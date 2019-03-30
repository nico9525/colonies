# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:41:10 2019

@author: juan.lopezl
"""
import cv2 as cv
import os  
import numpy as np

import matplotlib.pyplot as plt
# In[]
folders = ['05.04.2016','25.09.2015','26.04.2016']
# Imágenes del conteo automático
#gen_aut = 'Scripts/GUI/Resultados_GUI/'+folders[0]
#images_aut = []
#images_aut.append(os.listdir(gen_aut))
#images_aut = images_aut[0]
#images_aut = images_aut[14:]
#images_aut.pop(6)
#images_aut.pop(10)

# *** Otros programas ***
gen_aut = 'Resultados_OpenCFU/'+folders[0]
images_aut = []
images_aut.append(os.listdir(gen_aut))
images_aut = images_aut[0]
#images_aut.pop(6)
#images_aut.pop(10)
# *** Imágenes del conteo manual ***
gen = 'Fotos/Imagenes_Manual/'+folders[0]
images = []
images.append(os.listdir(gen))
images = images[0]

# In[]
#plt.close('all')
j=2
i=1
#kernel = np.ones([2,2])
#for i in range(0,7):
#PATH = 'Imagenes/' + folder_ids[j] + '/' + image_ids[j][i]

img = cv.imread(gen_aut+'/'+images_aut[1])  
m = img.shape

mit = img[0:round(m[0]/2)+20,0::,:]
plt.figure()
plt.imshow(mit,cmap='gray')
plt.show()


#m = img.shape
cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)      
#    cimg = cv.medianBlur(cimg,1)  
#    cimg = cv.equalizeHist(cimg)
#    cimg = cv.Canny(cimg, 0,0)
#    cimg = cv.dilate(cimg,kernel,iterations = 1)
#    cimg = cv.morphologyEx(cimg, cv.MORPH_CLOSE,(1,1))
#    cimg = cimg - (cv.GaussianBlur(cimg,(11,11),1))
#    histr = cv.calcHist([cimg],[0],None,[256],[0,256]) 
#m = np.shape(cimg)
##    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,(round(m[0]/5)*2),param1=26,param2=24,minRadius=round(m[0]/5)-3,maxRadius=round(m[0]/5)+12)
circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,(round(m[0]/5)*2),param1=26,param2=20,minRadius=round(m[0]/5)-1,maxRadius=round(m[0]/5)+12)

circles = np.uint8(np.around(circles)).reshape((6, 3))
#circles = circles[circles[:,1].argsort()]
#centro = np.copy(circles)

#for i in [0,3]:
#    for j in range(0,3):
#        if i+j < 5 and circles[i+j,0] > circles[i+j+1,0]:
#            T =  np.copy(circles[i+j,:])
#            circles[i+j,:] = circles[i+j+1,:]
#            circles[i+j+1,:] = T
# In[] Test
cv.destroyAllWindows()


gen = 'Fotos/Imagenes_Manual/'+folders[0]
images = []
images.append(os.listdir(gen))
images = images[0]

num_imgs = len(images)

for img in range(0,num_imgs):
    I = cv.imread(gen+'/'+images[img])
    Ic = cv.cvtColor(I,cv.COLOR_BGR2GRAY)
#    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,(round(m[0]/5)*2),param1=26,param2=20,minRadius=round(m[0]/5)-1,maxRadius=round(m[0]/5)+12)
#    circles = np.uint8(np.around(circles)).reshape((6, 3))
    circles = houghCircle(Ic)
    len_circles = len(circles[:,1])
    for j in range(0,len_circles):
        cv.circle(I,(circles[:,0][j],circles[:,1][j]),2,(0,255,0),-1)
    
    
#    print(len_circles)
    
    cv.namedWindow(images[img])
    cv.imshow(images[img],I)
    
#    plt.show()


# In[]            
def houghCircle(img):
#    cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)      
    m = cimg.shape
    
    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,(round(m[0]/5)*2),param1=26,param2=20,minRadius=round(m[0]/5)-1,maxRadius=round(m[0]/5)+12)
    circles = np.uint8(np.around(circles)).reshape((circles.shape[1], circles.shape[2]))
#    circles = circles[circles[:,1].argsort()]
    
    d = []
    for i in range(0,circles.shape[0]):
        d.append( np.sqrt( circles[:,0][i]**2 + circles[:,1][i]**2 ) )
        
    
    org =  np.argsort(d)
    circles = circles[org]
    return circles
