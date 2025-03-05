import time

import config
import services
from manager import Manager


def cancel_order_and_create_new(manager: Manager) -> None:
    """
    Скасування ордера продажу та створення нового
    """
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.MY_ORDERS_CANCEL_SELL_ORDERS[0],
        manager.start_cord[1] + config.MY_ORDERS_CANCEL_SELL_ORDERS[1]
    )

    time.sleep(1.5)
    services.move_lots_to_bag(manager)

    ok = manager.buy_order_cord = manager.search_image(
        f'templates_img/ok.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]],
        search_time=0.1
    )
    if ok:
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + ok[0],
            manager.start_cord[1] + ok[1]
        )

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.SECTION_SELL[0],
        manager.start_cord[1] + config.SECTION_SELL[1]
    )

    time.sleep(0.2)
    services.input_lot(manager)
    time.sleep(0.2)
    btn_sell = manager.buy_order_cord = manager.search_image(
        f'templates_img/btn_sell.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]],
        search_time=0.1
    )
    if not btn_sell:
        return
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + btn_sell[0],
        manager.start_cord[1] + btn_sell[1]
    )
    time.sleep(0.2)
    services.order_menu_sell_order(manager)
