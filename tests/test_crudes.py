from pyhcomet import crudes
from tests.conftest import skip_in_ci


def test_get_crude():
    res = crudes.get_crude("ABO2010")
    assert res is not None


def test_get_crudes():
    res = crudes.get_crudes()
    assert res is not None


@skip_in_ci
def test_get_crude_library():
    res = crudes.get_crude_library()
    assert res is not None
