from typing import Any, List, Type

from bluer_options.logger import logger


def are_01(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        int,
        lambda x: x in (0, 1),
        "{} is neither 0 nor 1.",
        log=log,
    )


def are_bools(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        bool,
        lambda x: True,
        "should not be printed",
        log=log,
    )


def are_ints(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        int,
        lambda x: True,
        "should not be printed",
        log=log,
    )


def are_nonempty_strs(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        str,
        bool,
        "empty str.",
        log=log,
    )


def are_positive_floats(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        float,
        lambda x: x > 0,
        "{:02f} <= 0!",
        log=log,
    )


def are_positive_ints(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        int,
        lambda x: x > 0,
        "{} <= 0!",
        log=log,
    )


def are_strs(
    things: Any,
    log: bool = False,
) -> bool:
    return are_func_things(
        things,
        str,
        lambda x: True,
        "should not be printed",
        log=log,
    )


def are_func_things(
    things: Any,
    type: Type,
    func,
    error_message: str,
    log: bool = False,
) -> bool:
    if not isinstance(things, list):
        if log:
            logger.error(f"{things.__class__.__name__} is not a list.")
        return False

    for thing in things:
        if not isinstance(thing, type):
            if log:
                logger.error(
                    "{}: {} expected, {} found.".format(
                        thing,
                        type,
                        thing.__class__.__name__,
                    )
                )
            return False

        if not func(thing):
            if log:
                logger.error(error_message.format(thing))

            return False

    return True


def is_list_of_str(
    things: Any,
    log: bool = False,
):
    return are_func_things(
        things,
        str,
        lambda x: True,
        "you must never see this!",
        log=log,
    )
