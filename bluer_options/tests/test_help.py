import pytest

from bluer_options.help.parsing import get_callable_module, get_callable_suffix


@pytest.mark.parametrize(
    ["callable", "expected_module_name"],
    [
        ["bluer_ai_git", "bluer_ai"],
        ["bluer_ai_git_push", "bluer_ai"],
        ["void_xyz", "void_xyz"],
        ["void_xyz_abc_dddsf", "void_xyz_abc_dddsf"],
    ],
)
def test_get_callable_module(
    callable: str,
    expected_module_name: str,
):
    assert get_callable_module(callable) == expected_module_name


@pytest.mark.parametrize(
    ["callable", "expected_suffix"],
    [
        ["bluer_ai_git", "git"],
        ["bluer_ai_git_push", "git_push"],
        ["void_xyz", ""],
        ["void_xyz_abc_dddsf", ""],
    ],
)
def test_get_callable_suffix(
    callable: str,
    expected_suffix: str,
):
    assert get_callable_suffix(callable) == expected_suffix
