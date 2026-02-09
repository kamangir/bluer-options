from bluer_options.web.access.check import check
from bluer_options.env import abcli_is_github_workflow


def test_web_access_check():
    success = check("void")
    assert not success

    url = "https://cnn.com" if abcli_is_github_workflow else "https://iribnews.ir"
    success = check(
        url,
        timeout=4,
    )
    assert success
