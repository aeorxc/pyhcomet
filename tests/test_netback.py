from tests import test_prices, test_slates, test_cases
from pyhcomet import netback, cases, price_sets, slates


def test_run_netback():
    res = netback.run_netback_case(18798)
    assert res is not None


def test_run_case_and_get_report():
    region = "NWE"
    price_set_template = test_prices.get_price_set_template()
    price_sets.post_price_set(price_set_template, region_id=region)
    price_set_id = int(price_sets.get_price_set_by_name(region, price_set_template["Name"])["ID"].iloc[0])
    slate_template = test_slates.get_slate_template()
    slates.post_slate(slate_template)
    slate_id = int(slates.get_slate_by_name(slate_template["Name"])["ID"].iloc[0])

    case_template = test_cases.get_case_template(price_set_id=price_set_id, slate_id=slate_id, region=region)
    cases.post_case(case_template)
    case_id = cases.get_case_by_name(case_template["Name"])["ID"].iloc[0]

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
