import cv2
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

photo_directory_downloaded = "../img/baixadas"
photo_directory_edited = "../img/editadas"

#TODO DEIXAR GERAL, PRA QUALQUER PARTICIPANTE
#TODO MELHORAR TRANSPARENCIA DO BABU
#TODO MUDAR PERSPECTIVA DO ROSTO
#TODO MELHORAR RECONHECIMENTO DE ROSTO


def face_recognition(img_with_faces):
    gray = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Se der empty eh pq o face cascade nao esta sendo carregado
    #print(face_cascade.empty())
    faces_found = face_cascade.detectMultiScale(gray, 1.2, 5)
    logger.info(" Foram encontrados {} rostos na figura".format(faces_found.shape[0]))
    return faces_found


# transp_img_over = babu
# background_img = foto a ser mashed up c/ a do babu
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
        # dim rosto do babu
        h_os, w_os = transparent_image_overlay.shape[0:2]
        logger.info(" Dimensoes do personagem: {} {}".format(w_os, h_os))
        personagem_ratio = h_os/w_os
        logger.info(" Ratio do personagem: {}".format(personagem_ratio))
        #transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), overlay_size)  # pegando copia da foto do babu para dar resize com as dim. detectadas
        # cv2.INTER_CUBIC eh slow segundo o opencv, testar dps ver se faz diferenca no result
        #transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), None, fx=face_ratio, fy=overlay_size[1], interpolation = cv2.INTER_LINEAR)(
        transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), overlay_size, interpolation = cv2.INTER_LINEAR)
        logger.info(" Tamanho depois do 1o resize: {}".format(transparent_image_overlay.shape))
        transparent_image_overlay = cv2.resize(transparent_image_overlay.copy(), None, fx=1, fy=personagem_ratio, interpolation = cv2.INTER_LINEAR)
        logger.info(" Tamanho depois do 2o resize: {}".format(transparent_image_overlay.shape))
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


def main(keywords):
    participante, user = keywords
    downloaded_photo_path = os.path.join(photo_directory_downloaded, participante, user + ".jpg")
    edited_photo_path = os.path.join(photo_directory_edited, participante, user + ".jpg")
    logger.info(" Caminho da imagem baixada: {}".format(downloaded_photo_path))
    #logger.info(" Caminho da imagem editada: {}".format(edited_photo_path))
    logger.info(" Carregando a imagem do participante {}".format(participante))
    # -1 carrega a img com fundo transparente
    participante_img_path = os.path.join("../img/", participante + ".png")
    logger.info(" Carregando imagem do participante: {}".format(participante_img_path))
    participante_img = cv2.imread(participante_img_path, -1)
    #cv2.imshow('teste', participante_img)
    img = cv2.imread(downloaded_photo_path)
    faces = face_recognition(img)

    # No caso de 3 faces, o for fara 3 iteracoes
    for (x, y, w, h) in faces:

        img = overlay_transparent(img, participante_img, x, y, (w, h))
        logging.info("Um novo rosto foi transformado no de {}".format(participante))
    cv2.imwrite(edited_photo_path, img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    main(["rafa", "danmascandrade"])