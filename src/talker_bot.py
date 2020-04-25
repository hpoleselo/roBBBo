import tweepy
import logging
import os
from twitter_config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

photo_directory = "../img/editadas"

def talker_bot(api, tweet, pessoa):
    logger.info("Iniciando o bot falador")
    user = tweet.user.screen_name
    logger.info("Vou responder o tweet de {}".format(user))
    try:
        if not tweet.user.id == api.me().id:
            filename = os.path.join(photo_directory, pessoa, user + ".jpg")
            logger.info("Caminho do arquivo: {}".format(filename))
            media = api.media_upload(filename)
            if pessoa == "babu":
                mensagem = "Deixa o paizão ganhar! #robbobabu"
            elif pessoa == "manu":
                mensagem = "Exército das fadas sensatas, me ajudem a ganhar! #robbbomanu"
            elif pessoa == "rafa":
                mensagem = "Vote pra eu ganhar com todos os seus jeitos falas, andados posicionamentos, etc #robbborafa"
            elif pessoa == "thelma":
                mensagem "Inimigos do fim, me ajudem a ganhar esse jogo! #robbbothelma" 
            api.update_status(status=mensagem, in_reply_to_status_id=tweet.id, media_ids=[media.media_id], auto_populate_reply_metadata=True)
            logger.info("Tweet postado")
        else:
            logger.info("O tweet é seu mesmo, não vou repostar")
    except Exception as e:
        logging.info("Erro ao postar tweet, erro:" + str(e))