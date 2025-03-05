import time
import effortless
import config
import services
from manager import Manager
from utils.create_buy_order import create_buy_order
from .cancel_order_and_create_new import cancel_order_and_create_new


def work_with_my_orders(manager: Manager) -> None:
    """
    Блок работы с разделом мои ордера, и все его логика
    """
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.SECTION_MY_ORDERS[0],
        manager.start_cord[1] + config.SECTION_MY_ORDERS[1]
    )
    effortless.random_delay(0.15,0.25)
    services.input_lot(manager)
    effortless.random_delay(0.3,0.4)

    profit = (manager.sell_price - manager.buy_price) / manager.buy_price
    print(profit)
    if profit < manager.actual_lot['min_profit']:
        services.close_buy_orders(manager)
        return
    time.sleep(0.4)
    amount_sell_orders = services.get_amount_sell_orders(manager)

    effortless.random_delay(0.3, 0.4)

    if amount_sell_orders == 0:
        duration_buy_order = services.get_duration_buy_order(manager)
        if not duration_buy_order:
            services.close_buy_orders(manager)
            create_buy_order(manager)
        elif duration_buy_order > manager.actual_lot['time_update']:
            # ОПОВЕЩЕНИЕ ОШИБКИ ПОКУПКИ
            services.send_problem_on_server(manager, 'PROBLEM WITH BUY')
            services.close_buy_orders(manager)
            create_buy_order(manager)

    elif amount_sell_orders == 1 or amount_sell_orders == 2:
        duration_sell_order = services.get_duration_sell_order(manager)
        duration_buy_order = services.get_duration_buy_order(manager)
        if duration_sell_order > manager.actual_lot['time_update']:
            # ОПОВЕЩЕНИЕ ОШИБКИ ПРОДАЖИ
            services.send_problem_on_server(manager, 'PROBLEM WITH SELL')
            cancel_order_and_create_new(manager)
        elif not duration_buy_order:
            services.close_buy_orders(manager)
            create_buy_order(manager)
        elif duration_buy_order > manager.actual_lot['time_update']:
            # ОПОВЕЩЕНИЕ ОШИБКИ ПОКУПКИ
            services.send_problem_on_server(manager, 'PROBLEM WITH BUY')
            services.close_buy_orders(manager)
            create_buy_order(manager)

    elif amount_sell_orders > 2:
        services.close_buy_orders(manager)
        duration_sell_order = services.get_duration_sell_order(manager)
        if duration_sell_order and (duration_sell_order > manager.actual_lot['time_update']):
            services.send_problem_on_server(manager, 'PROBLEM WITH SELL')
            cancel_order_and_create_new(manager)

    return

    # get_amount_sell_orders = 1
    # duration_buy_order = 1
    # duration_sell_order = 1
