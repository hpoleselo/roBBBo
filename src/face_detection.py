import numpy as np
import cv2

#TODO: VER PARAMETRO DE ESTICAMENTO DO BABU (1.3 em y pra ajustar o encaixe da face) entra
#TODO: tamanho variar de acordo com o tamanho do rosto
#TODO TROCAR ESSAS PORRAS DESSES PRINTS POR LOGGING
#TODO DEIXAR GERAL, PRA QUALQUER PARTICIPANTE
#TODO MELHORAR TRANSPARENCIA DO BABU
#TODO MUDAR PERSPECTIVA DO ROSTO
#TODO MELHORAR RECONHECIMENTO DE ROSTO

babu = cv2.imread('babu.png', -1)
img = cv2.imread('photo1.jpg')


def face_recognition(img_with_faces):
    gray = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Se der empty eh pq o face cascade nao esta sendo carregado
    #print(face_cascade.empty())

    #TODO VER ESSES PARAMETROS SE MELHROAM ALGUMA COISA
    # Ja retorna uma matriz Nx4 onde N eh o numero de faces detectadas
    faces_found = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces_found


def overlay_transparent(background_img, transparent_image_overlay, x, y, overlay_size=None):
    """
    	@brief      Coloca uma imagem com transparência por cima de outra que não tem transparência

    	Acho que tem passar (x,y) no overlay_size, pra ele dar o resize
    	@param      background_img    The background image
    	@param      transparent_image_overlay  The transparent image to overlay (has alpha channel)
    	@param      x                 x location to place the top-left corner of our overlay
    	@param      y                 y location to place the top-left corner of our overlay
    	@param      overlay_size      The size to scale our overlay to (tuple), no scaling if None

    	@return     Background image with overlay on top
    	"""
    bg_img = background_img.copy()

    if overlay_size is not None:
        transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), overlay_size)

    # Extract the alpha mask of the RGBA image, convert to RGB
    b, g, r, a = cv2.split(transparent_image_overlay)
    overlay_color = cv2.merge((b, g, r))

    # Apply some simple filtering to remove edge noise
    mask = cv2.medianBlur(a, 5)

    h, w, _ = overlay_color.shape
    roi = bg_img[y:y + h, x:x + w]

    # Black-out the area behind the logo in our original ROI
    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))

    # Mask out the logo from the logo image.
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

    # Update the original image with our new ROI
    bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return bg_img


faces = face_recognition(img)
# No caso de 3 faces, o for fara 3 iteracoes
for (x,y,w,h) in faces:
    imagem_editada = overlay_transparent(img, babu, x, y, (w, h))
    cv2.imshow('provisoria-{}'.format(x), imagem_editada)

cv2.imshow('osso', imagem_editada)
cv2.waitKey(0)
cv2.destroyAllWindows()