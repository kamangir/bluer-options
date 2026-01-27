from bluer_options import string
from bluer_options import env


def as_str(
    emoji: bool = True,
    timestamp: bool = False,
) -> str:
    pass_ = "✅" if emoji else "pass"
    fail = "🛑" if emoji else "fail"

    return "{} storage {}, web {}".format(
        (
            "{} -".format(
                string.timestamp(
                    unique_length=0,
                )
            )
            if timestamp
            else "access:"
        ),
        pass_ if env.BLUER_AI_STORAGE_IS_ACCESSIBLE else fail,
        pass_ if env.BLUER_AI_WEB_IS_ACCESSIBLE else fail,
    )
