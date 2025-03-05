import effortless
import pyperclip
import keyboard
import time
import config
from manager import Manager


def input_lot(manager: Manager) -> None:
    # Сбрасываю название товара
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + manager.back_row_cord[0],
        manager.start_cord[1] + manager.back_row_cord[1]
    )
    effortless.random_delay(0.2, 0.3)

    # Активирую полле ввода
    manager.mouse_controller.move_and_click(
        manager.start_cord[0] + manager.back_row_cord[0] + config.BACK_ROW_SHIFT_FOR_ENTER[0],
        manager.start_cord[1] + manager.back_row_cord[1] + config.BACK_ROW_SHIFT_FOR_ENTER[1]
    )

    enter_lot = f'{manager.actual_lot["name"]} {manager.actual_lot["tier"]}.{manager.actual_lot["enchantment"]}'
    pyperclip.copy(enter_lot)
    effortless.random_delay(0.2, 0.3)
    keyboard.press_and_release('ctrl + v')
