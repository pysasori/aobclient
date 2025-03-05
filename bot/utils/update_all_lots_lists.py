import services
from manager import Manager


def update_all_lots_lists(manager: Manager) -> None:
    """
    Оновлення списків товарі(з серва)
    """
    main_list = manager.main_list
    new_list = services.get_lots_data_from_server()
    ids_in_new_list = {item['id'] for item in new_list}
    manager.remove_list = [item for item in main_list if item['id'] not in ids_in_new_list]
    manager.main_list = new_list
