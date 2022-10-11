from pyhcomet import refineries
import pytest

def test_get_refinary_list():
    res = refineries.get_refinary_list('NWE','GERMANY')
    assert res is not None

def test_get_refinary():
    res = refineries.get_refinary('NWE',1)
    assert res is not None

def test_get_refinary_configs():
    res = refineries.get_refinary_configs('NWE')
    assert res is not None

def test_get_refinary_config():
    res = refineries.get_refinary_config('NWE',1)
    assert res is not None

