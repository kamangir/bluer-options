import pytest

from bluer_options.web.access.vars import dict_of_variables
from bluer_options.testing.dicts import is_a_dict


@pytest.mark.parametrize(
    ["for_logging"],
    [
        [True],
        [False],
    ],
)
def test_web_access_vars(
    for_logging: bool,
):
    dict_of_variables_ = dict_of_variables(
        for_logging=for_logging,
    )

    assert is_a_dict(
        dict_of_variables_,
        key_type=str,
        value_type=dict,
    )
