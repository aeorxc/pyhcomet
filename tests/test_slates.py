from pyhcomet import slates
import pytest

def test_get_slates():
    res = slates.get_slates()
    assert res is not None

def test_get_slate():
    res = slates.get_slate()
    assert res is not None