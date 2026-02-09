import pytest

from bluer_options.web.access.vars import dict_of_variables
from bluer_options.testing.dicts import is_a_flat_dict


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
    assert is_a_flat_dict(
        dict_of_variables(
            for_logging=for_logging,
        ),
        key_type=str,
        value_type=int,
    )
