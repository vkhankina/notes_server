from google.oauth2 import id_token
from google.auth.transport import requests
from config import config


class GoogleAuth():
    @staticmethod
    def verify_token(token):
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), config.GOOGLE_OAUTH_CLIENT_ID)
        return idinfo['sub']
