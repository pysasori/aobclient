import time
import keyboard

from manager import Manager
import config


def enter_to_npc_and_get_back_row(manager: Manager) -> None:
    """
    Вхід в аукціон + додавання back_row до manager
    """
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.DEFAULT_SHIFT_START[0],
        manager.start_cord[1] + config.DEFAULT_SHIFT_START[1]
    )
    time.sleep(0.2)
    keyboard.press_and_release('esc')
    time.sleep(0.3)
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + config.NPC_CORDS[0],
        manager.start_cord[1] + config.NPC_CORDS[1]
    )
    time.sleep(0.3)

    manager.back_row_cord = manager.search_image(
        'templates_img/back_row.bmp',
        cords=[manager.start_cord[0], manager.start_cord[1], config.LEN_WINDOW[0], config.LEN_WINDOW[1]]
    )
