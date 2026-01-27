import pytest

from bluer_options.web.access import as_str


@pytest.mark.parametrize(
    ["emoji"],
    [
        [False],
        [True],
    ],
)
@pytest.mark.parametrize(
    ["timestamp"],
    [
        [False],
        [True],
    ],
)
def test_web_access(
    emoji: bool,
    timestamp: bool,
):
    value = as_str(
        emoji=emoji,
        timestamp=timestamp,
    )
    assert isinstance(value, str)
    assert value
