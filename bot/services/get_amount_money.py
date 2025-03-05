import config
import services
from manager import Manager


def get_amount_money(manager: Manager) -> int:
    amount_money = manager.amount_money(
        [
            manager.start_cord[0] + config.AMOUNT_MONEY_CORD[0],
            manager.start_cord[1] + config.AMOUNT_MONEY_CORD[1],
            75,
            25
        ]

    )
    if 'k' in amount_money:
        amount_money = services.remove_non_digits_and_get_int(amount_money) * 1000
    elif 'm' in amount_money:
        amount_money = services.remove_non_digits_and_get_int(amount_money) * 1000 * 1000

    return amount_money
