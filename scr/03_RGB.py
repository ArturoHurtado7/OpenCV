import cv2
import numpy as np

#Default Image comes from BGR
bgr = np.zeros((300,300,3),dtype=np.uint8) 

#black
cv2.imshow('BGR',bgr)
cv2.waitKey(0)

#blue
bgr[:,:,:]=(255,0,0)
cv2.imshow('BGR',bgr)
cv2.waitKey(0)

#green
bgr[:,:,:]=(0,255,0)
cv2.imshow('BGR',bgr)
cv2.waitKey(0)

#*******************************************
#BGR2RBG

#BGR
bgr = cv2.imread('Photos/maimy.jpg')
cv2.imshow('Color',bgr)

#Divide in diferents chanels
C1 = bgr[:,:,0]
C2 = bgr[:,:,1]
C3 = bgr[:,:,2]
cv2.imshow('BGR',np.hstack([C1,C2,C3]))
#cv2.waitKey(0)

#RGB
rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
C1 = rgb[:,:,0]
C2 = rgb[:,:,1]
C3 = rgb[:,:,2]
cv2.imshow('RGB',np.hstack([C1,C2,C3]))

#GREY
grey=cv2.cvtColor(bgr,cv2.COLOR_RGB2GRAY)
cv2.imshow('Grey',grey)

#Espera
cv2.waitKey(0)

#destroy all windows
cv2.destroyAllWindows()



