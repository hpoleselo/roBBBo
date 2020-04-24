import cv2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#TODO DEIXAR GERAL, PRA QUALQUER PARTICIPANTE
#TODO MELHORAR TRANSPARENCIA DO BABU
#TODO MUDAR PERSPECTIVA DO ROSTO
#TODO MELHORAR RECONHECIMENTO DE ROSTO

logger.info("Carregando a imagem do participante...")
# -1 carrega a img com fundo transparente
babu = cv2.imread('../img/babu.png', -1)
img = cv2.imread('../img/photo1.jpg')


def face_recognition(img_with_faces):
    gray = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Se der empty eh pq o face cascade nao esta sendo carregado
    #print(face_cascade.empty())
    faces_found = face_cascade.detectMultiScale(gray, 1.2, 5)
    logger.info("Foram encontrados {} rostos na figura".format(faces_found.shape[0]))
    return faces_found


# transp_img_over = babu
# background_img = foto a ser mashed up c/ a do babu

#def overlay_transparent(background_img, transparent_image_overlay, x, y, overlay_size=None):
def overlay_transparent(background_img, transparent_image_overlay, x, y, overlay_size):
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
        # dim rosto do babu
        w_os, h_os = transparent_image_overlay.shape[0:2]
        babu_ratio = h_os/w_os 
        #face_ratio = overlay_size[1]/overlay_size[0]
        #transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), overlay_size)  # pegando copia da foto do babu para dar resize com as dim. detectadas
        # cv2.INTER_CUBIC eh slow segundo o opencv, testar dps ver se faz diferenca no result
        transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), None, fx=babu_ratio, fy=babu_ratio, interpolation = cv2.INTER_LINEAR) 
        cv2.imshow('resized', transparent_image_overlay)
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
# TODO: ver mais pra frente pra ir iterando (adicionando um indice?) a cada imagem nova, ja que o programa vai rodar de forma continua
# Criei essa pasta img_edit pra enviar as editadas, nao sei o que vai ser mais facil nessa parte da API do twitter... 
cv2.imwrite('../img_edit/teste.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()