import pytest

from pyhcomet import crudes


def test_get_crude():
    res = crudes.get_crude("ABO2010")
    assert res is not None


def test_get_crudes():
    res = crudes.get_crudes()
    assert res is not None


@pytest.mark.skip(reason="Not authorised")
def test_get_crude_library():
    res = crudes.get_crude_library()
    assert res is not None
