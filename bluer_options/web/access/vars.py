from typing import Dict

from bluer_options import env

dict_of_variables: Dict[str, Dict] = {
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
