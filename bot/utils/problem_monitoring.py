import time
import keyboard

import config
from manager import Manager
import services


def problem_monitoring(manager: Manager) -> None:
    """
    Моніторинг кількості помилок і реакції на них
    """
    manager.error_count += 1

    if manager.error_count <= 5:
        for i in range(3):
            keyboard.press_and_release('esc')
        manager.mouse_controller.move_and_click(
            manager.start_cord[0] + config.NPC_CORDS[0],
            manager.start_cord[1] + config.NPC_CORDS[1]
        )
    if 10 > manager.error_count > 5:
        services.restart_client(manager)
    elif manager.error_count > 10:
        services.restart_client(manager)
        services.send_tg_error()
        time.sleep(60)
