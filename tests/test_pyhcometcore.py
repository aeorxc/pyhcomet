import pytest
from pyhcomet import hcometcore


def test_token():
    res = hcometcore.get_token()
    assert res is not None
