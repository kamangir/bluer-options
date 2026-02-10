from typing import Any, Type

from bluer_options.logger import logger


def is_a_dict(
    things: Any,
    key_type: Type = str,
    value_type: Type = int,
    log: bool = False,
) -> bool:
    if not isinstance(things, dict):
        if log:
            logger.error(f"{things.__class__.__name__} is not a dict.")
        return False

    for key, value in things.items():
        if not isinstance(key, key_type):
            if log:
                logger.error(
                    "the key: {}, is a {}, not a {}.".format(
                        key,
                        key.__class__.__name__,
                        key_type,
                    )
                )
            return False

        if not isinstance(value, value_type):
            if log:
                logger.error(
                    "the value: {}, is a {}, not a {}.".format(
                        value,
                        value.__class__.__name__,
                        value_type,
                    )
                )
            return False

    return True
