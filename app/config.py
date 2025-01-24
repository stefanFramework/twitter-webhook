import os
from os.path import join

from dotenv import load_dotenv

load_dotenv(join(os.path.dirname(__file__), '.env.cesar'))


class WebhookConfig:
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    API_KEY = os.getenv('API_KEY')
    API_KEY_SECRET = os.getenv('API_KEY_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    WEBHOOK_ENV = os.getenv('WEBHOOK_ENV', 'development')
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')


current_config = WebhookConfig()

