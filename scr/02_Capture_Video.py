import cv2

#Captura del video por webcam, 0 - webcam, 1 - otra camara instalada
#capture = cv2.VideoCapture(0)

#Captura del video almacenado en memoria por nombre
capture = cv2.VideoCapture('Photos/videoSalida.mp4')

#Guarda el video
#Output = cv2.VideoWriter('Photos/videoSalida.mp4',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

while(capture.isOpened()):
    ret,imagen=capture.read()

    #Output.write(imagen)
    if ret == True:
        cv2.imshow('video', imagen)
        if cv2.waitKey(50) & 0xFF == ord('s'):
            break
    else:
        break

#Output.release()
capture.release()
cv2.destroyAllWindows()