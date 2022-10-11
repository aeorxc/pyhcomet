from pyhcomet import price_sets
import pytest

def test_get_price_sets():
    res = price_sets.get_price_sets('NWE')
    assert res is not None

def test_get_price_set():
    res = price_sets.get_price_set(119910)
    assert res is not None