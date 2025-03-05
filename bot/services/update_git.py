import effortless


def update_git() -> None:
    try:
        updater = effortless.AutoUpdater(updater=effortless.GitUpdater(), restart_on_update=True)
        updater.update_and_restart()
    except Exception as e:
        print(e)
