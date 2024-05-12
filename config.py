from dotenv import load_dotenv
from os import getenv
TOKEN = '7036098567:AAEW7SccjkpJVjmmhqM6zB2Yd7HcfTtmby4'
FOLDER_ID = "b1g3bcb59cje2qfhu2lr"
IAM_TOKEN = 't1.9euelZqRkcyRipmOy8-Ylo3Ix8ycme3rnpWaip7OnZWYzpLPmZKXjs6bjJ7l8_ccHH1N-e8_RD96_d3z91xKek357z9EP3r9zef1656VmpqTz5aalpPLmY-MzJyKxo-N7_zF656VmpqTz5aalpPLmY-MzJyKxo-NveuelZqRjs2NmsadjMjOypWNnZaKzrXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.mLfhmvhKeX7A30R3lyrI5XmT_lTH1ZKfk9e_gutWg63bc6U_NaOvE96o9Vu2f4BbSU0vT5oeClEnnUXGn-hJAw'

filename="log_file.txt"
MAX_USERS = 3
MAX_GPT_TOKENS = 120
COUNT_LAST_MSG = 4
TOKENIZE_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenizeCompletion"
GPT_MODEL = 'yandexgpt-lite'
GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
MAX_USER_STT_BLOCKS =15
MAX_USER_TTS_SYMBOLS = 5_000
MAX_USER_GPT_TOKENS = 3_000
DB_FILE = 'messages.db'
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Будь добрым другом пользователя'}]
LOGS = 'creds/logs.log'
