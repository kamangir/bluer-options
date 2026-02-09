from typing import Any, Type

from bluer_options.logger import logger


def is_a_flat_dict(
    thing: Any,
    key_type: Type,
    value_type: Type,
    log: bool = False,
) -> bool:
    if not isinstance(thing, dict):
        if log:
            logger.error(f"{thing.__class__.__name__} is not a dict.")
        return False

    for key, value in thing.items():
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
