from typing import Any
import pytest

from bluer_options.testing import are_nonempty_strs
from bluer_options.tests.test_testing_are import list_of_assets


@pytest.mark.parametrize(
    ["list_of_things", "expected_output"],
    [
        [
            asset["list_of_things"],
            asset["are_nonempty_strs"],
        ]
        for asset in list_of_assets
    ],
)
def test_testing_are_nonempty_strs(
    list_of_things: Any,
    expected_output: bool,
):
    assert (
        are_nonempty_strs(
            list_of_things,
            log=True,
        )
        == expected_output
    ), list_of_things
