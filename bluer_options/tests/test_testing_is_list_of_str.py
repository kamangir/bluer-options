from typing import Any
import pytest

from bluer_options.testing import is_list_of_str
from bluer_options.tests.test_testing_are import list_of_assets


@pytest.mark.parametrize(
    ["list_of_things", "expected_output"],
    [
        [
            asset["list_of_things"],
            asset["is_list_of_str"],
        ]
        for asset in list_of_assets
    ],
)
def test_testing_is_list_of_str(
    list_of_things: Any,
    expected_output: bool,
):
    assert is_list_of_str(list_of_things) == expected_output, list_of_things
