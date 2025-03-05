import time

import config
from manager import Manager


def close_buy_orders(manager: Manager) -> None:
    for i in range(3):
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + config.MY_ORDERS_CANCEL_BUY_ORDERS[0],
            manager.start_cord[1] + config.MY_ORDERS_CANCEL_BUY_ORDERS[1]
        )
        time.sleep(0.1)
