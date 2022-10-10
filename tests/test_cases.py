from pyhcomet import cases
import pytest


def test_get_cases():
    res = cases.get_cases()
    assert res is not None


def test_get_case():
    res = cases.get_case(18644)
    assert res is not None
