import time
import keyboard
import services

from manager import Manager
import config


def get_prices(manager: Manager) -> [int, int]:
    pull_out_menu = manager.search_image(
        'templates_img/pull_out_menu.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]],
        search_time=0.1
    )
    if pull_out_menu:
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + pull_out_menu[0],
            manager.start_cord[1] + pull_out_menu[1]
        )

    manager.search_image(
        f'templates_img/silver_coin.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1] / 2]

    )
    time.sleep(0.08)

    sell_price = manager.scan_prices([
        manager.start_cord[0] + config.SELL_ORDER_PRICE[0],
        manager.start_cord[1] + config.SELL_ORDER_PRICE[1],
        config.ORDER_PRICE_ZONE[0],
        config.ORDER_PRICE_ZONE[1]
    ])
    print(sell_price)

    buy_price = manager.scan_prices([
        manager.start_cord[0] + config.BUY_ORDERS_PRICE[0],
        manager.start_cord[1] + config.BUY_ORDERS_PRICE[1],
        config.ORDER_PRICE_ZONE[0],
        config.ORDER_PRICE_ZONE[1]
    ])

    print(buy_price)

    return services.remove_non_digits_and_get_int(sell_price), services.remove_non_digits_and_get_int(buy_price)
