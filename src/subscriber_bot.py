import tweepy
import logging
import json
import os
from twitter_config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

photo_directory = "../fotos_editadas"


class hashtagListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        try:
            if 'media' in tweet.entities:
                for image in tweet.entities['media']:
                    logger.info("Tem uma imagem aí")
                    photoOwner = tweet.user.screen_name
                    picName = "editada_%s.jpg" % photoOwner
                    link = image['media_url']
                    filename = os.path.join
            else:
                logger.info("Esse post não tem imagem")
        except:
            logger.error("Erro ao favoritar tweet")

def main(keywords):
    api = create_api()
    tweets_listener = hashtagListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords)

if __name__ == "__main__":
    main(["#testebotbbb"])
    print("Starting up program")