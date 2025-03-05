import effortless

import services
from manager import Manager
import config


def check_and_get_prices(manager: Manager) -> None:
    """
    Отримання ціни товару який у роботі, та додавання його до менеджера
    """
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.SECTION_CREATE_BUY_ORDERS[0],
        manager.start_cord[1] + config.SECTION_CREATE_BUY_ORDERS[1]
    )
    effortless.random_delay(0.1, 0.2)
    services.input_lot(manager)
    effortless.random_delay(0.2, 0.3)

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

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + manager.buy_order_cord[0],
        manager.start_cord[1] + manager.buy_order_cord[1]
    )

    manager.search_image(
        f'templates_img/silver_coin.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1] / 2]

    )

    manager.sell_price, manager.buy_price = services.get_prices(manager)

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.EXIT_FROM_ORDERS[0],
        manager.start_cord[1] + config.EXIT_FROM_ORDERS[1]
    )
    effortless.random_delay(0.25, 0.4)
