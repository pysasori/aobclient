import requests
import config
from services import read_from_file


def get_seller_data_from_server():
    """Отправляет POST-запрос на сервер"""
    try:
        data = {
            "name": read_from_file(config.SELLER_NUMBER_FILE_PATH)
        }
        url = f"{config.SERVER_URL}{config.SERVER_URL_SELLER_INFO}"
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=data, headers=headers, timeout=config.REQUEST_TIMEOUT)
        response.raise_for_status()

        print(f"✅ Успешный запрос. Статус: {response.status_code}")
        return response.json()

    except FileNotFoundError as e:
        print(f"❌ Ошибка: {e}")
    except ValueError as e:
        print(f"❌ Ошибка: {e}")
    except requests.Timeout:
        print("❌ Ошибка: Таймаут запроса")
    except requests.RequestException as e:
        print(f"❌ Ошибка запроса: {e}")
