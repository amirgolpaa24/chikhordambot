import json
import os

with open('credentials.json', 'r') as f:
    credentials = json.load(f)
    
    # Telegram
    API_TOKEN = credentials['API_TOKEN']

    # Database
    DB_HOST_NAME = credentials['DB_HOST_NAME']
    DB_HOST_NAME_EXTERNAL = credentials['DB_HOST_NAME_EXTERNAL']
    DB_PORT = credentials['DB_PORT']
    DB_NAME = credentials['DB_NAME']
    DB_USERNAME = credentials['DB_USERNAME']
    DB_PASSWORD = credentials['DB_PASSWORD']
    DB_INTERNAL_URL = credentials['DB_INTERNAL_URL']
    DB_EXTERNAL_URL = credentials['DB_EXTERNAL_URL']
    DB_PSQL_COMMAND = credentials['DB_PSQL_COMMAND']
    
    # OpenAI
    OPENAI_API_KEY = credentials['OPENAI_API_KEY']
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
