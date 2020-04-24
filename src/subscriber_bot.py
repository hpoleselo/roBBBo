import tweepy
import logging
import json
import os
import urllib
from twitter_config import create_api
from talker_bot import talker_bot


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
                    picName = "%s.jpg" % photoOwner
                    link = image['media_url']
                    filename = os.path.join(photo_directory, picName)
                    # talvez vamos ter que usar o agent (https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c)
                    urllib.request.urlretrieve(link, filename)

                    talker_bot(self.api, tweet)
            else:
                logger.info("Esse post não tem imagem")
        except Exception as e:
            logger.error("Erro ao favoritar tweet, erro:" + str(e))

def main(keywords):
    api = create_api()
    tweets_listener = hashtagListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords)

if __name__ == "__main__":
    main(["#testebotbbb"])
    print("Starting up program")