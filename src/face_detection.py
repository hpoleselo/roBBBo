import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Se der empty eh pq o face cascade nao esta sendo carregado
#print(face_cascade.empty())

babu = cv2.imread('babu.jpg')
img = cv2.imread('photo1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Ja retorna uma matriz Nx4 onde N eh o numero de faces detectadas
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# No caso de 3 faces, o for fara 3 iteracoes
for (x,y,w,h) in faces: 

    # tamanho do rosto
    print(x)
    print(w)
    
    # tamanho do rosto
    size_x = int(x) - int(w)
    print(type(size_x))
    
    #size_x = xtmp - wtmp
    print("Tamanho do rosto em x: "), size_x
    size_y = y - h

    # de acordo com as medidas do rosto iriamos entao ajustar com um resizing/rescaling
    # pega a foto do babu
    #print("Tamanho do rosto em x: "), size_x
    #print("Tamanho do rosto em y: "), size_y
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    #for (ex,ey,ew,eh) in eyes:
    #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)   
cv2.waitKey(0)
cv2.destroyAllWindows()