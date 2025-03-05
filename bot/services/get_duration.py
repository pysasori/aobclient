import config
from manager import Manager
from services.remove_non_digits_and_get_int import remove_non_digits_and_get_int


def get_duration_buy_order(manager: Manager)-> None | int:
    return get_duration(manager, config.DURATION_BUY_ORDERS)


def get_duration_sell_order(manager: Manager)-> None | int:
    return get_duration(manager, config.DURATION_SELL_ORDERS)


def get_duration(manager: Manager, cords: list[int]) -> None | int:
    try:
        days = manager.scan_prices([
            manager.start_cord[0] + cords[0],
            manager.start_cord[1] + cords[1],
            config.DURATION_ORDERS_ZONE_SEARCH[0],
            config.DURATION_ORDERS_ZONE_SEARCH[1]
        ])
        hours = manager.scan_prices([
            manager.start_cord[0] + cords[0] + config.DURATION_SHIFT_FROM_D_TO_H[0],
            manager.start_cord[1] + cords[1] + config.DURATION_SHIFT_FROM_D_TO_H[1],
            config.DURATION_ORDERS_ZONE_SEARCH[0],
            config.DURATION_ORDERS_ZONE_SEARCH[1]
        ])
        print('days', days)
        print('hours', hours)
        return 720 - (remove_non_digits_and_get_int(days) * 24 + remove_non_digits_and_get_int(hours))
    except:
        return None
