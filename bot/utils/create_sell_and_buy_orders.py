import time
import effortless

import config
import services
from manager import Manager


def create_sell_and_buy_orders(manager: Manager) -> None:
    """
    Отримує лут із закритих угод в інвентар, і виставляє нові ордери
    """
    get_lots = services.move_lots_to_bag(manager)
    if not get_lots:
        return

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

    effortless.random_delay(0.2, 0.3)
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + manager.back_row_cord[0],
        manager.start_cord[1] + manager.back_row_cord[1]
    )
    effortless.random_delay(0.2, 0.35)

    while True:

        btn_sell = manager.buy_order_cord = manager.search_image(
            f'templates_img/btn_sell.bmp',
            cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]],
            search_time=1.5
        )
        if not btn_sell:
            return
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + btn_sell[0],
            manager.start_cord[1] + btn_sell[1]
        )
        effortless.random_delay(0.1, 0.2)

        manager.search_image(
            f'templates_img/silver_coin.bmp',
            cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1] / 2]

        )

        sell_price, buy_price = services.get_prices(manager)
        if not sell_price:
            services.order_menu_sell_order_without_sell_price(manager, buy_price)
            continue
        elif not buy_price:
            time.sleep(0.1)

        else:
            profit = (sell_price - buy_price) / buy_price
            if profit > 0.15:
                services.order_menu_buy_order(manager)
                effortless.random_delay(0.25, 0.35)
                manager.mouse_controller.move_and_click(
                    manager.start_cord[0] + btn_sell[0],
                    manager.start_cord[1] + btn_sell[1]
                )
                effortless.random_delay(0.25, 0.35)
        services.order_menu_sell_order(manager)

        effortless.random_delay(0.2, 0.35)
