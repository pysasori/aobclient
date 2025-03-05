import time

import requests
import config
from services import read_from_file, send_tg_error



def get_lots_data_from_server():
    """Отправляет POST-запрос на сервер"""
    try:
        data = {
            "name": read_from_file(config.SELLER_NUMBER_FILE_PATH)
        }
        url = f"{config.SERVER_URL}{config.SERVER_URL_SELLER_PRODUCTS}"
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=data, headers=headers, timeout=config.REQUEST_TIMEOUT)
        response.raise_for_status()

        print(f"✅ Успешный запрос. Статус: {response.status_code}")
        return response.json()

    except Exception as e:
        send_tg_error(f'Проблема с сервером на машинке {read_from_file(config.SELLER_NUMBER_FILE_PATH)}')
        time.sleep(60)




