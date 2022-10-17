import time

import pandas as pd


from pyhcomet import cases, price_sets, slates


def test_get_cases():
    res = cases.get_cases()
    assert res is not None
    if len(res) > 0:
        id = res['ID'].iloc[0]
        res = cases.get_case(id)
        assert res is not None


def get_case_template(price_set_id: int, slate_id: int, region: str):
    case_name = f"test_case_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    template = cases.case_template(SimplePriceSetID=price_set_id, SlateID=slate_id, RegionID=region, Name=case_name)
    return template


def test_post_case():
    price_set_id = price_sets.get_price_sets(region_id="NWE")['ID'].iloc[0]
    slate_id = slates.get_slates()["ID"].iloc[0]
    template = get_case_template(price_set_id=price_set_id, slate_id=slate_id, region="NWE")
    res = cases.post_case(template)
    assert res == 'Created'
    time.sleep(1)
    testcase = cases.get_case_by_name(template["Name"])
    res = cases.delete_case(testcase['ID'].iloc[0])
    assert res == 'No Content'

