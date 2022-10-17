import time

import pandas as pd

from pyhcomet import cases


def test_get_cases():
    res = cases.get_cases()
    assert res is not None


def test_get_case():
    res = cases.get_case(18644)
    assert res is not None


def test_post_case():
    case_name = f"test_case_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    template = {
        'Selected': True,
        # 'Comment': '',
        'SlateOrBlend': '',
        'SlateID': "",
        'BlendID': "",
        'CutSetID': None,
        'ModelType': 0,
        'RegionID': "NWE",
        'PriceSetType': 0,
        'SimplePriceSetID': 195731,
        'SimplePriceSetGroupID': None,
        'SimpleRefineryConfigID': 72193,
        'SimpleSpecificationID': 1884,
        'SimpleCutSetID': 0,
        'SimpleSeasonCode': 'INT',
        'Name': case_name
    }
    res = cases.post_case(template)
    assert res == 'Created'
    time.sleep(1)
    allcases = cases.get_cases()
    testcase = allcases[allcases['Name'] == case_name]
    res = cases.delete_case(testcase['ID'].iloc[0])
    assert res == 'No Content'
