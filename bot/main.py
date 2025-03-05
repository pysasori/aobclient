import time
import random

import services
import utils
import config
from manager import Manager

if __name__ == "__main__":

    while True:
        manager = Manager()
        try:
            # Авто оновлення с гіта,
            services.update()

            # Оновлення продавця
            utils.update_seller_data(manager)

            # Оновлення списків товарів
            utils.update_all_lots_lists(manager)

            # Отправка в сон
            utils.sleep_queue(manager)

            manager.start_cord = manager.search_image('templates_img/icon_game.bmp')
            if not manager.start_cord:
                time.sleep(6)
                services.restart_client(manager)
                continue
            else:
                manager.mouse_controller.move_and_click(
                    manager.start_cord[0] + config.DEFAULT_SHIFT_START[0],
                    manager.start_cord[1] + config.DEFAULT_SHIFT_START[1]
                )
            while True:

                # Надсилання срібла на серв та оновлення обсягу товару на сервері
                utils.update_amount_lots(manager)

                # Оновлення продавця
                utils.update_seller_data(manager)

                # Оновлення списків товарів
                utils.update_all_lots_lists(manager)

                # Вход в ніпа і полученя корд стрілки
                utils.enter_to_npc_and_get_back_row(manager)

                for i in manager.remove_list:
                    try:

                        manager.actual_lot = i

                        utils.remove_list(manager)

                    except Exception as e:
                        print(e)

                main_list = manager.main_list[:manager.amount_lots].copy()
                random.shuffle(main_list)
                for i in main_list:
                    try:

                        # Отправка в сон
                        utils.sleep_queue(manager)

                        print(i)

                        manager.actual_lot = i

                        utils.check_and_get_prices(manager)

                        utils.work_with_my_orders(manager)

                        utils.create_sell_and_buy_orders(manager)

                        manager.error_count = 0

                    except Exception as e:
                        import traceback

                        print(f"Ошибка: {e}")
                        print("Трасування помилки:")
                        print(traceback.format_exc())

                        utils.problem_monitoring(manager)
                        utils.enter_to_npc_and_get_back_row(manager)



        except Exception as e:
            utils.problem_monitoring(manager)
            print(e)
            time.sleep(1)
