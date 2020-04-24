import tweepy
import logging
from twitter_config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def talker_bot(api, tweet):
    logger.info("Iniciando o bot falador")
    user = tweet.user.screen_name
    logger.info("Vou responder o tweet de {}".format(user))
    try:
        #if not tweet.user.id == api.me().id:
        media = api.media_upload("../fotos_editadas/{}.jpg".format(user))
        api.update_status(status="Teste oficial", in_reply_to_status_id=tweet.id, media_ids=[media.media_id], auto_populate_reply_metadata=True)
        logger.info("Tweet postado")
        #else:
        #    logger.info("O tweet é seu mesmo, não vou repostar")
    except Exception as e:
        logging.info("Erro ao postar tweet, erro:" + str(e))