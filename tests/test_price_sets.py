import time

import pandas as pd

from pyhcomet import price_sets


def test_get_price_sets():
    res = price_sets.get_price_sets("NWE")
    assert res is not None
    if len(res) > 0:
        id = res["ID"].iloc[0]
        res = price_sets.get_price_set("NWE", id)
        assert res is not None


def test_build_price_set_template():
    prices = [
        {"Description": "LPG", "Price": 650, "Unit": "$/MT"},
    ]
    res = price_sets.price_set_template(prices, "test_price_set")
    assert res is not None


def test_submit_price_set():
    prices = [
        {"Description": "LPG", "Price": 650, "PriceUnit": "$/MT"},
        {"Description": "Naphtha", "Price": 750, "PriceUnit": "$/MT"},
    ]
    name = f"test_price_set_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    set_id = price_sets.submit_price_set(prices=prices, region_id="NWE", name=name)
    assert set_id is not None
    time.sleep(1)
    res = price_sets.delete_set(region_id="NWE", set_id=set_id)
    assert res == "No Content"
