import requests

from blueness import module

from bluer_options import NAME
from bluer_options import env
from bluer_options import string
from bluer_options.timing import ElapsedTimer
from bluer_options.logger import logger


NAME = module.name(__file__, NAME)


def check(
    url,
    timeout: int = 3,
    verbose: bool = False,
) -> bool:
    forced_offline: bool = env.BLUER_AI_FORCE_OFFLINE == 1

    if verbose:
        logger.info(
            "{}.check[timeout={}]({})?{}".format(
                NAME,
                string.pretty_duration(
                    timeout,
                    short=True,
                ),
                url,
                " [⛓️‍💥 forced offline]" if forced_offline else "",
            )
        )

    if forced_offline:
        return False

    success = False
    elapsed_timer = ElapsedTimer()
    try:
        response = requests.get(
            url,
            timeout=timeout,
        )
        success = response.status_code == 200
    except Exception as e:
        if verbose:
            logger.warning(e)

    if verbose:
        logger.info(
            "{} in {}.".format(
                "succeeded" if success else "failed",
                elapsed_timer.as_str(),
            )
        )

    return success
