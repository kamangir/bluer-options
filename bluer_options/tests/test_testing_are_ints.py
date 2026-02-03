from typing import Any
import pytest

from bluer_options.testing import are_ints
from bluer_options.tests.test_testing_are import list_of_assets


@pytest.mark.parametrize(
    ["list_of_things", "expected_output"],
    [
        [
            asset["list_of_things"],
            asset["are_ints"],
        ]
        for asset in list_of_assets
    ],
)
def test_testing_are_are_ints(
    list_of_things: Any,
    expected_output: bool,
):
    assert (
        are_ints(
            list_of_things,
            log=True,
        )
        == expected_output
    ), list_of_things
