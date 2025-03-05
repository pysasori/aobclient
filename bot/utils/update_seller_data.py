import services
from manager import Manager


def update_seller_data(manager: Manager) -> None:
    """
    Оновлення данних продавця
    """
    new_list = services.get_seller_data_from_server()
    manager.amount_lots = new_list['amount_lots']
    manager.time_sleep_from = new_list['time_sleep_from']
    manager.time_sleep_to = new_list['time_sleep_to']

