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
        {"Code": "LPG", "Price": 650, "Unit": "$/MT"},
    ]
    res = price_sets.price_set_template(prices, "test_price_set")
    assert res is not None


def get_price_set_template():
    price_set = (
        f"test_price_set_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    )

    prices = [
        {"Description": "LPG", "Price": 650, "PriceUnit": "$/MT"},
        {"Description": "Naphtha", "Price": 750, "PriceUnit": "$/MT"},
    ]

    template = price_sets.price_set_template(prices, name=price_set)

    return template


def test_post_price_set():
    template = get_price_set_template()
    res = price_sets.post_price_set(template, region_id="NWE")
    assert res == "Created"
    time.sleep(1)
    testset = price_sets.get_price_set_by_name("NWE", set_name=template["Name"])
    res = price_sets.delete_set(region_id="NWE", set_id=testset["ID"].iloc[0])
    assert res == "No Content"
