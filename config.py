from dotenv import load_dotenv
from os import getenv
TOKEN = '7036098567:AAEW7SccjkpJVjmmhqM6zB2Yd7HcfTtmby4'
FOLDER_ID = "b1g3bcb59cje2qfhu2lr"
IAM_TOKEN = 't1.9euelZrIlZPOzoqcyInJyo2LzcaWy-3rnpWaip7OnZWYzpLPmZKXjs6bjJ7l8_cpHQJO-e8ebTI2_t3z92lLf0357x5tMjb-zef1656VmpLHmZWMnpPImMmNzoyVmZbG7_zF656VmpLHmZWMnpPImMmNzoyVmZbGveuelZqLns6Unc2Vx86QmY6JyZTNnLXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.GeJimnabMKqDykNaKVJ-Yqbe3bj2PLaMnpKTDL0ndiF3E2qEuyxJ0V0a3DoofI_sRfQvqiUSliUjt1onuwF0Cw'
ADMINS_IDS = getenv('1250982438')  # list
filename="log_file.txt"
MAX_USERS = 3
MAX_GPT_TOKENS = 120
COUNT_LAST_MSG = 4
TOKENIZE_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenizeCompletion"
GPT_MODEL = 'yandexgpt-lite'
GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
MAX_USER_STT_BLOCKS = 13
MAX_USER_TTS_SYMBOLS = 5_000
MAX_USER_GPT_TOKENS = 2_000
DB_FILE = 'messages.db'
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Будь добрым другом пользователя'}]
LOGS = 'creds/logs.log'
