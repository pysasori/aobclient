from datetime import datetime
import time

import services
from manager import Manager


def sleep_queue(manager: Manager) -> None:
    """
    Черга сну
    """
    now = datetime.now()
    print(manager.time_sleep_from, manager.time_sleep_to)
    print(now.hour)
    if manager.time_sleep_from <= now.hour < manager.time_sleep_to:
        print(f'BOT sleep until {manager.time_sleep_to}')
        services.kill_process_by_window_name("Albion-Online.exe")
        time.sleep(1)
        services.kill_process_by_window_name("AlbionLauncher.exe")
        time.sleep(1)
        services.kill_process_by_window_name("Albion-Online_BE.exe")
        next_run = now.replace(hour=manager.time_sleep_to, minute=0, second=0)

        sleep_time = (next_run - now).total_seconds()

        time.sleep(sleep_time)

        services.restart_client(manager)
