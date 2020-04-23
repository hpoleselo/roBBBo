import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():

    api_key = os.getenv("API_KEY")
    api_secret_key = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # autenticar usuário
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    # criando ligacao com a api do twitter - rate limit eh o limite de requisicoes do tt
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Erro na autenticação")
        raise e
    logger.info("Autenticação Feita")
    logger.info("API criada")
    return api
