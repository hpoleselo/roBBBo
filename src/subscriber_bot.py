import logging
import argparse
import json
import os
import urllib
import tweepy
# Nossos scripts
from twitter_config import create_api
from talker_bot import talker_bot
import face_detection

logger = logging.getLogger(__name__)
photo_directory = "../img/baixadas"


class hashtagListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        try:
            if 'hashtags' in tweet.entities:
                # 0 pra pegar a primeira hashtag, 6: pra tirar o robbbo
                pessoa = tweet.entities['hashtags'][0]["text"][6:]
                logger.info("Novo tweet torcendo para {}".format(pessoa))
            if 'media' in tweet.entities:
                for image in tweet.entities['media']:
                    photoOwner = tweet.user.screen_name
                    logger.info("Pegando imagem do tweet de {}".format(photoOwner))
                    picName = "%s.jpg" % photoOwner
                    link = image['media_url']
                    filename = os.path.join(photo_directory, pessoa, picName)
                    # talvez vamos ter que usar o agent (https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c)
                    urllib.request.urlretrieve(link, filename)
                    face_detection.main([pessoa, photoOwner])
                    talker_bot(self.api, tweet, pessoa)
            else:
                logger.info("Esse post não tem imagem")
        except Exception as e:
            logger.exception("Erro ao favoritar tweet, erro:")

def main(keywords):
    import logging.config
    logging.config.fileConfig('loggers.conf', disable_existing_loggers=False)
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", action='store_true', help="Aciona o modo Debug do logging.")
    args = parser.parse_args()
    if args.v:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Nível do logger: {}".format(logging.getLogger().level))
    api = create_api()
    tweets_listener = hashtagListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    #Streams do not terminate unless the connection is closed, blocking the thread. Tweepy offers a convenient is_async parameter on filter so the stream will run on a new thread. For example
    stream.filter(track=keywords)
    logger.debug(" Escutando a hashtag...")

if __name__ == "__main__":
    main(["#roBBBoBabu", "#roBBBoManu", "#roBBBoRafa", "roBBBoThelma"])


