import requests
import config
from services import read_from_file
from manager import Manager


def send_problem_on_server(manager: Manager, text_error:str):
    """Отправляет ошибку на сервер"""
    try:
        data = {
            "product_id": manager.actual_lot['id'],
            "name": read_from_file(config.SELLER_NUMBER_FILE_PATH),
            "description": text_error
        }
        url = f"{config.SERVER_URL}{config.SERVER_URL_PROBLEM}"
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




