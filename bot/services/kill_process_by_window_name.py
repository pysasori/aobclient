import psutil


def kill_process_by_window_name(window_name: str) -> None:
    for proc in psutil.process_iter(['pid', 'name']):

        if proc.info['name'] == window_name:
            print('убиваем window_name')
            proc.kill()
