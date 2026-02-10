import numpy as np

from bluer_options.web.access.vars import dict_of_variables


def get_color() -> str:
    heat = "55"

    dict_of_variables_ = dict_of_variables()

    if not dict_of_variables_["pypi"]["value"]:
        # blue
        return f"0000{heat}"

    if not dict_of_variables_["web"]["value"]:
        # yellow
        return f"{heat}{heat}00"

    if not dict_of_variables_["cloud"]["value"]:
        # red
        return f"{heat}0000"

    return "000000"
