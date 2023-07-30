import torch
import cv2
import numpy as np

# leo el modelo
model = torch.hub.load('ultralytics/yolov5', 
                       'custom', 
                       path='C:/Users/bastian/Desktop/definitivo/best (1).pt')


cap = cv2.VideoCapture(0)
while True:
    # realizo la lectura de la video captura
    ret, frame = cap.read()
    detect = model(frame)
    
    #muestro fps
    cv2.imshow('Señaleticas', np.squeeze(detect.render()))

    t = cv2.waitKey(5)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()