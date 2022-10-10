from pyhcomet import netback
import pytest


def test_run_netback():
    res = netback.run_netback_case(18751)
    assert res is not None


def test_get_run_status():
    res = netback.get_run_status(2)
    assert res is not None


def test_get_report():
    res = netback.get_report(1)
    assert res is not None