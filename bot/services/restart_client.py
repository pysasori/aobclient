import time
import keyboard
from manager import Manager
from .kill_process_by_window_name import kill_process_by_window_name


def restart_client(manager: Manager) -> None:
    try:
        kill_process_by_window_name("Albion-Online.exe")
        time.sleep(2)
        kill_process_by_window_name("AlbionLauncher.exe")
        time.sleep(2)
        kill_process_by_window_name("Albion-Online_BE.exe")
        time.sleep(5)

        keyboard.press('win')
        time.sleep(0.1)
        keyboard.press_and_release('1')
        time.sleep(0.1)
        keyboard.release('win')

        time.sleep(10)

        play = manager.search_image(
            'templates_img/play.bmp',
            search_time=30
        )
        if play:
            manager.mouse_controller.move_and_click(play[0], play[1])
            time.sleep(140)
        else:
            time.sleep(600)
            return

        enter_world = manager.search_image(
            'templates_img/enter_world.bmp',
            search_time=30
        )
        if not enter_world:
            time.sleep(600)
            login = manager.search_image(
                'templates_img/login.bmp',
                search_time=5
            )
            if login:
                manager.mouse_controller.move_and_click(login[0], login[1])
                time.sleep(10)
                enter_world = manager.search_image(
                    'templates_img/enter_world.bmp',
                    search_time=10
                )
        if enter_world:
            manager.mouse_controller.move_and_click(enter_world[0], enter_world[1])

            time.sleep(13)
            keyboard.press_and_release('esc')
            time.sleep(2)
    except:
        ## NEED FiX
        print('OY')
