import effortless
import keyboard
import pyperclip

import config
from manager import Manager


def order_menu_buy_order(manager: Manager) -> None:
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + manager.buy_order_cord[0],
        manager.start_cord[1] + manager.buy_order_cord[1]
    )
    effortless.random_delay(0.4, 0.5)
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_CREATE_BUY_ORDER_CHECKPOINT[0],
        manager.start_cord[1] + config.ORDER_CREATE_BUY_ORDER_CHECKPOINT[1]
    )

    effortless.random_delay(0.1, 0.15)

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_PRICE_BTN_PLUS[0],
        manager.start_cord[1] + config.ORDER_PRICE_BTN_PLUS[1]
    )

    effortless.random_delay(0.1, 0.15)

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_DTN_CREATE[0],
        manager.start_cord[1] + config.ORDER_DTN_CREATE[1]
    )
    effortless.random_delay(0.15, 0.2)
    cords_yes = manager.buy_order_cord = manager.search_image(
        f'templates_img/yes.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]]
    )

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + cords_yes[0],
        manager.start_cord[1] + cords_yes[1]
    )


def order_menu_sell_order(manager: Manager) -> None:
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_CREATE_SELL_ORDER_CHECKPOINT[0],
        manager.start_cord[1] + config.ORDER_CREATE_SELL_ORDER_CHECKPOINT[1]
    )
    effortless.random_delay(0.1, 0.15)
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_PRICE_BTN_MINUS[0],
        manager.start_cord[1] + config.ORDER_PRICE_BTN_MINUS[1]
    )
    effortless.random_delay(0.1, 0.15)

    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_DTN_CREATE[0],
        manager.start_cord[1] + config.ORDER_DTN_CREATE[1]
    )


def order_menu_sell_order_without_sell_price(manager: Manager, buy_price) -> None:
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_CREATE_SELL_ORDER_CHECKPOINT[0],
        manager.start_cord[1] + config.ORDER_CREATE_SELL_ORDER_CHECKPOINT[1]
    )
    effortless.random_delay(0.1, 0.15)
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_PRICE_INPUT[0],
        manager.start_cord[1] + config.ORDER_PRICE_INPUT[1]
    )
    effortless.random_delay(0.1, 0.15)

    pyperclip.copy(buy_price * 1.23)
    effortless.random_delay(0.2, 0.3)
    keyboard.press_and_release('ctrl + v')
    effortless.random_delay(0.1, 0.15)
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.ORDER_DTN_CREATE[0],
        manager.start_cord[1] + config.ORDER_DTN_CREATE[1]
    )
