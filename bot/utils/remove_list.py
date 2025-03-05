import time

import effortless

import config
from manager import Manager
import services


def remove_list(manager: Manager) -> None:
    """
    Закриття неактуальних ордерів
    """
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.SECTION_MY_ORDERS[0],
        manager.start_cord[1] + config.SECTION_MY_ORDERS[1]
    )
    effortless.random_delay(0.2, 0.3)
    services.input_lot(manager)
    effortless.random_delay(0.32, 0.4)
    services.close_buy_orders(manager)
