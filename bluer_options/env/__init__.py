from typing import Union

from bluer_options.env.functions import load_config, load_env, get_env

load_config(__name__)


ABCUL = " \\\n\t"


bluer_ai_log_filename = get_env("bluer_ai_log_filename")


CYAN = "\033[36m"
GREEN = "\033[32m"
LIGHTBLUE = "\033[96m"
NC = "\033[0m"
RED = "\033[31m"

EOP = "\033[33m"

HOST_NAME: Union[None, str] = None

abcli_hostname = get_env("abcli_hostname")

BLUER_AI_WIFI_SSID = get_env("BLUER_AI_WIFI_SSID")

BLUER_OPTIONS_TIMEZONE = get_env("BLUER_OPTIONS_TIMEZONE")

abcli_is_rpi4 = get_env("abcli_is_rpi4")

abcli_is_rpi5 = get_env("abcli_is_rpi5")

BLUER_AI_INTERNET_INSIDE_IS_ACCESSIBLE = get_env(
    "BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE", 1
)
BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE = get_env(
    "BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE", 1
)

BLUER_AI_INTERNET_STATUS: str = ""
if BLUER_AI_INTERNET_INSIDE_IS_ACCESSIBLE:
    if BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE:
        BLUER_AI_INTERNET_STATUS = "online"
    else:
        BLUER_AI_INTERNET_STATUS = "national"
else:
    if BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE:
        BLUER_AI_INTERNET_STATUS = "-national"
    else:
        BLUER_AI_INTERNET_STATUS = "offline"