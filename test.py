"""
pytest test.py
"""
import pytest


def test_normal_case():
    assert 1 == 1, "wrong"


@pytest.fixture(scope="module")
def global_val():
    """
    means you can call it value globally
    https://docs.pytest.org/en/stable/fixture.html
    """
    return "IamGlobalVariable"


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_param_eval(test_input, expected):
    assert eval(test_input) == expected
