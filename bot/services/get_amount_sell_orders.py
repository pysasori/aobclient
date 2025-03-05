import config
from manager import Manager


def get_amount_sell_orders(manager: Manager) -> int:
    for i in range(4):
        pull_out_menu = manager.search_image(
            'templates_img/edit.bmp',
            cords=[
                manager.start_cord[0] + config.MY_ORDERS_EDIT_4_LOT[0],
                manager.start_cord[1] + config.MY_ORDERS_EDIT_4_LOT[1] - (50 * i),
                config.MY_ORDERS_EDIT_4_LOT_ZONA[0],
                config.MY_ORDERS_EDIT_4_LOT_ZONA[1]
            ],
            search_time=0.1
        )
        if pull_out_menu:
            return 4 - i

    return 0
