from pyhcomet import crudes
import pytest


def test_get_crude():
    res = crudes.get_crude('ABO2010')
    assert res is not None

