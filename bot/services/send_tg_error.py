import effortless
from services import read_from_file
import config


def send_tg_error(text:str='')-> None:
    effortless.send_telegram_message(
        api_token="1951848439:AAE6Gp86G-TVd6RrgJHHf7N1NQN7SEnUF7M",
        chat_id=-1001941678039,
        text=f'Проблема у бота {read_from_file(config.SELLER_NUMBER_FILE_PATH)}, {text}'
    )