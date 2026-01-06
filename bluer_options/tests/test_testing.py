from typing import Any
import pytest

from bluer_options.testing import is_list_of_str


@pytest.mark.parametrize(
    ["thing", "expected_output"],
    [
        [1, False],
        [[1, 2, 3], False],
        ["this", False],
        [{"this": "that"}, False],
        [[{"this": "that"}], False],
        [["this", ["that"]], False],
        [[], True],
        [["this", "that"], True],
    ],
)
def test_testing_is_list_of_str(
    thing: Any,
    expected_output: bool,
):
    assert is_list_of_str(thing) == expected_output
