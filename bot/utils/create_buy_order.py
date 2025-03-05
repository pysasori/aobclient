import time

import services
from manager import Manager
import config


def create_buy_order(manager: Manager) -> None:
    """
    Просте створення ордера купівлі товару
    """
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.SECTION_CREATE_BUY_ORDERS[0],
        manager.start_cord[1] + config.SECTION_CREATE_BUY_ORDERS[1]
    )
    time.sleep(0.2)
    # services.input_lot(manager)
    # time.sleep(0.2)

    lots_img_cord = manager.search_image(
        f'lots_img/{manager.actual_lot["image"]}.png',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0] / 2, config.LEN_WINDOW[1]]
    )

    manager.buy_order_cord = manager.search_image(
        f'templates_img/buy_order.bmp',
        cords=[
            lots_img_cord[0], lots_img_cord[1],
            config.BTN_CREATE_ORDER_ZONE_SEARCH[0], config.BTN_CREATE_ORDER_ZONE_SEARCH[1]
        ]
    )
    services.order_menu_buy_order(manager)
