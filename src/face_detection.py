import cv2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#TODO: VER PARAMETRO DE ESTICAMENTO DO BABU (1.3 em y pra ajustar o encaixe da face) entra
#TODO SALVAR IMAGEM EM ARQUIVO
#TODO DEIXAR GERAL, PRA QUALQUER PARTICIPANTE
#TODO MELHORAR TRANSPARENCIA DO BABU
#TODO MUDAR PERSPECTIVA DO ROSTO
#TODO MELHORAR RECONHECIMENTO DE ROSTO

logger.info("Carregando a imagem do participante")
# -1 carrega a img transparente
babu = cv2.imread('img/babu.png', -1)
img = cv2.imread('img/photo1.jpg')


def face_recognition(img_with_faces):
    gray = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Se der empty eh pq o face cascade nao esta sendo carregado
    #print(face_cascade.empty())

    #TODO VER ESSES PARAMETROS SE MELHROAM ALGUMA COISA
    # Ja retorna uma matriz Nx4 onde N eh o numero de faces detectadas
    faces_found = face_cascade.detectMultiScale(gray, 1.3, 5)
    logger.info("Foram encontrados {} rostos na figura".format(faces_found.shape[0]))
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
        logging.info("Resizing da imagem feito, novo tamanho: {}x{}".format(overlay_size[0], overlay_size[1]))

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
    img = overlay_transparent(img, babu, x, y, (w, h))
    logging.info("Um novo rosto foi transformado no do Babu")

cv2.imshow('Imagem Editada', img)
cv2.waitKey(0)
cv2.destroyAllWindows()