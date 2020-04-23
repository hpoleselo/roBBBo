import tweepy
import logging
from twitter_config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def talker_bot(api):
    logger.info("Iniciando o bot falador")

    try:
        media = api.media_upload("bot.jpg")
        api.update_status("Primeiro tweet feito pelo meu bot #testebotbbb")
        logging.info("Tweet postado")
    except:
        logging.info("Erro ao postar tweet")