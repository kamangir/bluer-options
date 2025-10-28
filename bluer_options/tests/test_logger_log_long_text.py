import pytest

from bluer_options.logger import logger, log_long_text, shorten_text
from bluer_options import string


@pytest.mark.parametrize(
    ["text"],
    [
        [string.random(10)],
        [string.random(100)],
        [string.random(1000)],
    ],
)
@pytest.mark.parametrize(
    ["max_length"],
    [
        [11],
        [51],
        [101],
    ],
)
def test_log_long_text(
    text: str,
    max_length: int,
):
    text = shorten_text(text, max_length=max_length)
    assert isinstance(text, str)

    log_long_text(
        logger=logger,
        text=text,
        max_length=max_length,
    )
