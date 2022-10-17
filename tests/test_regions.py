from pyhcomet import regions
import pytest


def test_get_regions():
    res = regions.get_regions()
    assert res is not None
