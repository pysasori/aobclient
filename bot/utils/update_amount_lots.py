import services
from manager import Manager


def update_amount_lots(manager: Manager) -> None:
    """
    Обновить количество лотов на сервере, отправляя количество серебра
    """
    money = services.get_amount_money(manager)
    services.send_money_on_server(manager, money)
