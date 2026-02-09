from bluer_options import env
from bluer_options import string
from bluer_options.web.access.vars import dict_of_variables


def as_str(
    emoji: bool = True,
    timestamp: bool = False,
) -> str:
    return "{} {}{}".format(
        (
            "{} -".format(
                string.timestamp(
                    unique_length=0,
                )
            )
            if timestamp
            else "access:"
        ),
        ", ".join(
            [
                "{}{}".format(
                    name,
                    (
                        (" ✅" if emoji else "")
                        if info["value"]
                        else (" 🛑" if emoji else " X")
                    ),
                )
                for name, info in dict_of_variables.items()
            ]
        ),
        "⛓️‍💥 [ forced offline]" if env.BLUER_AI_FORCE_OFFLINE else "",
    )
