import effortless
import config
from manager import Manager


def move_lots_to_bag(manager: Manager):

    lots_was_bought = manager.buy_order_cord = manager.search_image(
        f'templates_img/lots_was_bought.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]],
        search_time = 0.1
    )

    if lots_was_bought:
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + lots_was_bought[0],
            manager.start_cord[1] + lots_was_bought[1]
        )
        effortless.random_delay(1.5, 2)
        take_all = manager.buy_order_cord = manager.search_image(
            f'templates_img/take_all.bmp',
            cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]],
            search_time=0.1
        )
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + take_all[0],
            manager.start_cord[1] + take_all[1]
        )
        effortless.random_delay(1, 1.2)
        return True

    return False


