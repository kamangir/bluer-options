from typing import Dict

from bluer_options import env


def dict_of_variables(
    for_logging: bool = False,
) -> Dict[str, Dict]:
    output = {
        "cloud": {
            "name": "BLUER_AI_CLOUD_IS_ACCESSIBLE",
            "value": env.BLUER_AI_CLOUD_IS_ACCESSIBLE,
        },
        "web": {
            "name": "BLUER_AI_WEB_IS_ACCESSIBLE",
            "value": env.BLUER_AI_WEB_IS_ACCESSIBLE,
        },
        "pypi": {
            "name": "BLUER_AI_PYPI_IS_ACCESSIBLE",
            "value": env.BLUER_AI_PYPI_IS_ACCESSIBLE,
        },
    }

    if not for_logging:
        output["forced_offline"] = {
            "name": "BLUER_AI_FORCE_OFFLINE",
            "value": env.BLUER_AI_FORCE_OFFLINE,
        }

    return output
