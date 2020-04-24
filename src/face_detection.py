import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Se der empty eh pq o face cascade nao esta sendo carregado
#print(face_cascade.empty())

babu = cv2.imread('babu.png', -1)
img = cv2.imread('photo1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
babu_height, babu_width = babu.shape[0:2] 

# Ja retorna uma matriz Nx4 onde N eh o numero de faces detectadas
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#TODO: VER PARAMETRO DE ESTICAMENTO DO BABU (1.3 em y pra ajustar o encaixe da face) entra
#TODO: tamanho variar de acordo com o tamanho do rosto

# No caso de 3 faces, o for fara 3 iteracoes
for (x,y,w,h) in faces:
    #babuzinho = cv2.resize(babu, (w, h))
    babuzinho = cv2.resize(babu, (255, 255))
    bg_img = img.copy()
    b, g, r, alpha = cv2.split(babuzinho)
    babu_colorido = cv2.merge((b,g,r))

    mascara = cv2.medianBlur(alpha,5)

    # s
    h,w,_ = babu_colorido.shape

    # area de interesse
    roi = img[y:y+h,x:x+w]
    # Black-out the area behind the logo in our original ROI
    img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask=cv2.bitwise_not(mascara))

    # Mask out the logo from the logo image.
    img2_fg = cv2.bitwise_and(babu_colorido,babu_colorido,mask = mascara)


    # Update the original image with our new ROI
    bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)


# Desenha as bounding boxes reconhecidas
#img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#roi_gray = gray[y:y+h, x:x+w]
#roi_color = img[y:y+h, x:x+w]

#cv2.imshow('img',babu)   
#cv2.imshow('babuzinh', babuzinho)
#cv2.imshow('imgweighted', img_final)
#cv2.imshow('famiglia', img) 
cv2.imshow('osso', bg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()