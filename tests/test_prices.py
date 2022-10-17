import time

import pandas as pd

from pyhcomet import price_sets


def test_get_price_sets():
    res = price_sets.get_price_sets('NWE')
    assert res is not None
    if len(res) > 0:
        id = res['ID'].iloc[0]
        res = price_sets.get_price_set("NWE", id)
        assert res is not None


def test_post_price_set():
    price_set = f"test_price_set_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"

    template = {
        "Products": [
            {
                'Code': 'LPG',
                'Description': 'LPG',
                'Selected': 'false',
                'Price': 650,
                'PriceUnit': '$/MT',
                'RateUnit': 'Vol%',
                'Number': 1,
                'Type': 0,
                'LPCode': 'LPG',
            },
            {
                'Code': 'LNA',
                'Description': 'Naphtha',
                'Selected': 'false',
                'Price': 700,
                'PriceUnit': '$/MT',
                'RateUnit': 'Vol%',
                'Number': 2,
                'Type': 0,
                'LPCode': 'LNA',
            },
        ],
        "Name": price_set,
    }
    res = price_sets.post_price_set(template, region_id="NWE")
    assert res == 'Created'
    time.sleep(1)
    allpriceslates = price_sets.get_price_sets("NWE")
    testset = allpriceslates[allpriceslates['Name'] == price_set]
    res = price_sets.delete_set(region_id="NWE", set_id=testset['ID'].iloc[0])
    assert res == 'No Content'
