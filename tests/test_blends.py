from pyhcomet import blends
import pytest

def test_get_blends():
    res = blends.get_blends()
    assert res is not None

def test_get_blend():
    res = blends.get_blend(44999)
    assert res is not None