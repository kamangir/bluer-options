import pytest
from typing import Callable, Union

from bluer_options.host.functions import (
    is_64bit,
    is_aws_batch,
    is_docker,
    is_ec2,
    is_github_workflow,
    is_headless,
    is_jetson,
    is_jupyter,
    is_mac,
    is_rpi,
    is_ssh_session,
    is_ubuntu,
    signature,
)


def test_signature():
    assert signature()


@pytest.mark.parametrize(
    ["func", "expected_value"],
    [
        [is_64bit, None],
        [is_aws_batch, None],
        [is_docker, None],
        [is_ec2, None],
        [is_github_workflow, None],
        [is_headless, False],
        [is_jetson, False],
        [is_jupyter, False],
        [is_mac, None],
        [is_rpi, False],
        [is_ssh_session, None],
        [is_ubuntu, None],
    ],
)
def test_host_is(
    func: Callable,
    expected_value: Union[bool, None],
):
    if expected_value is True:
        assert func()
    elif expected_value is False:
        assert not func()
    elif expected_value is None:
        assert isinstance(func(), bool)
    else:
        assert False, "Invalid expected_value"
