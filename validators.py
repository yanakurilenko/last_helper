import logging
import math
from config import MAX_USERS, MAX_USER_GPT_TOKENS, MAX_USER_STT_BLOCKS, MAX_USER_TTS_SYMBOLS
from database import count_users, count_all_limits
from database import add_message, create_database, select_n_last_messages
from gpt import count_gpt_tokens

import logging

from telebot import TeleBot
bot = TeleBot('7036098567:AAEW7SccjkpJVjmmhqM6zB2Yd7HcfTtmby4')

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

    filename="log_file.txt",

    filemode="w",

)

'''import os

# Путь к директории логов
log_directory = 'creds'
log_file = 'logs.log'
full_log_path = os.path.join(log_directory, log_file)
import logging

# Создание директории, если она не существует
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Создание файла логов, если он не существует
if not os.path.isfile(full_log_path):
    with open(full_log_path, 'w'):
        pass  # Просто создаем файл, если он еще не существует

# Теперь можно безопасно инициализировать логгер
logging.basicConfig(filename=full_log_path, level=logging.DEBUG,
                    format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="a")

logging.basicConfig(filename=LOGS, level=logging.DEBUG,
                    format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="a")
'''

def check_number_of_users(user_id):
    count = count_users(user_id)
    if count is None:
        return None, "Ошибка при работе с БД"
    if count > MAX_USERS:
        return None, "Превышено максимальное количество пользователей"
    return True, ""


def is_gpt_token_limit(messages, total_spent_tokens, user_id):
    all_tokens = count_gpt_tokens(messages) + total_spent_tokens
    if all_tokens > MAX_USER_GPT_TOKENS:
        return None, f"Превышен общий лимит GPT-токенов {MAX_USER_GPT_TOKENS}"
    return all_tokens, ""
    bot.send_message(message.from_user.id, 'Превышен общий лимит GPT-токенов {MAX_USER_GPT_TOKENS}')


def is_stt_block_limit(user_id, duration):
    audio_blocks = math.ceil(duration / 15)
    all_blocks = count_all_limits(user_id, 'stt_blocks') + audio_blocks

    if duration >= 30:
        response = "SpeechKit STT работает с голосовыми сообщениями меньше 30 секунд"
        return None, response
        bot.send_message(message.from_user.id, "SpeechKit STT работает с голосовыми сообщениями меньше 30 секунд")

    if all_blocks >= MAX_USER_STT_BLOCKS and str(user_id) not in ADMINS_IDS:
        response = (f"Превышен общий лимит SpeechKit STT {MAX_USER_STT_BLOCKS}. Использовано {all_blocks} блоков. "
                    f"Доступно: "f"{MAX_USER_STT_BLOCKS - all_blocks}")
        return None, response
        bot.send_message(message.from_user.id, "Превышен общий лимит SpeechKit STT {MAX_USER_STT_BLOCKS}. Использовано {all_blocks} блоков. ")

    return audio_blocks, None


def is_tts_symbol_limit(user_id, text):
    text_symbols = len(text)

    all_symbols = count_all_limits(user_id, 'tts_symbols') + text_symbols

    if all_symbols >= MAX_USER_TTS_SYMBOLS:
        msg = (f"Превышен общий лимит SpeechKit TTS {MAX_USER_TTS_SYMBOLS}. Использовано: {all_symbols} символов. "
               f"Доступно: {MAX_USER_TTS_SYMBOLS - all_symbols}")
        return None, msg
        bot.send_message(message.from_user.id, "Превышен общий лимит SpeechKit TTS {MAX_USER_TTS_SYMBOLS}. Использовано: {all_symbols} символов. ")

    return text_symbols, None
