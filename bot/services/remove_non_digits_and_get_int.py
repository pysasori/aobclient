import re


def remove_non_digits_and_get_int(text: str) -> int | None:
    try:
        str_remove_non_digits = re.sub(r'\D', '', text)
        return int(str_remove_non_digits)
    except:
        return None
