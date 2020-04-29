import tweepy
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_api():
    api_key = os.getenv("API_KEY")
    api_secret_key = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    if not api_key or not api_secret_key or not access_token or not access_token_secret:
        logger.error("Encerrando o programa, pelo menos uma key não foi definida")
        sys.exit()

    # autenticar usuário
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    # criando ligacao com a api do twitter - rate limit eh o limite de requisicoes do tt
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except:
        logger.exception("Erro na autenticação, finalizando a aplicação")
        sys.exit()
    logger.info("Autenticação Feita na api feita")
    return api

if __name__ == "__main__":
    create_api()