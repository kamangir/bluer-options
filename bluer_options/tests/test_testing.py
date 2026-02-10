from typing import Dict, Callable
import pytest

from bluer_options.testing.dicts import is_a_dict
from bluer_options.testing.lists import (
    are_01,
    are_bools,
    are_ints,
    are_nonempty_strs,
    are_positive_floats,
    are_positive_ints,
    are_strs,
    is_list_of_str,
)
from bluer_options.tests.test_testing_assets import list_of_assets


@pytest.mark.parametrize(
    ["asset"],
    [[asset] for asset in list_of_assets],
)
@pytest.mark.parametrize(
    ["func", "func_name"],
    [
        [is_a_dict, "is_a_dict"],
        [are_01, "are_01"],
        [are_bools, "are_bools"],
        [are_ints, "are_ints"],
        [are_nonempty_strs, "are_nonempty_strs"],
        [are_positive_floats, "are_positive_floats"],
        [are_positive_ints, "are_positive_ints"],
        [are_strs, "are_strs"],
        [is_list_of_str, "is_list_of_str"],
    ],
)
def test_testing(
    asset: Dict,
    func: Callable,
    func_name: str,
):
    assert func(
        things=asset["things"],
        log=True,
    ) == asset.get(
        func_name,
        False,
    ), (asset, func_name)
