import pandas as pd

from pyhcomet import netback, cases, price_sets, slates
from tests import test_cases


def test_run_case_and_get_report():
    region = "NWE"
    prices = [
        {"Description": "LPG", "Price": 650, "PriceUnit": "$/MT"},
        {"Description": "Naphtha", "Price": 750, "PriceUnit": "$/MT"},
    ]
    name = f"test_price_set_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    price_set_id = price_sets.submit_price_set(prices=prices, region_id=region, name=name)
    crudes = [
        {
            "Code": "AGBMI472",
            "Library": "CHEVRON_EQUITY",
        },
        {
            "Code": "AGBMI480",
            "Library": "CHEVRON_EQUITY",
        },
    ]
    name = f"test_slate_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    slate_id = slates.submit_slate(crudes=crudes, name=name)

    case_template = test_cases.get_case_template(
        price_set_id=price_set_id, slate_id=slate_id, region=region
    )
    case_id = cases.submit_case(case=case_template)

    res = netback.run_case_and_get_report(case_id)
    assert res is not None

    price_sets.delete_set(region, set_id=price_set_id)
    slates.delete_slate(slate_id)
    cases.delete_case(case_id)


def test_get_run_status():
    res = netback.get_run_status(2)
    assert res is not None


def test_get_report():
    res = netback.get_report(1)
    assert res is not None
