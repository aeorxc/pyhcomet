from pyhcomet import crude_price_sets
import pytest


def test_get_price_sets():
    res = crude_price_sets.get_crude_price_sets("NWE")
    assert res is not None


@pytest.mark.skip(reason="No permanent price set id at present")
def test_get_price_set():
    res = crude_price_sets.get_crude_price_set(195671)
    assert res is not None
