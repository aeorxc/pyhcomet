import time

import pandas as pd

from pyhcomet import slates


def test_get_slates():
    res = slates.get_slates()
    assert res is not None
    if len(res) > 0:
        id = res['ID'].iloc[0]
        res = slates.get_slate(id)
        assert res is not None


def get_slate_template():
    slate_name = f"test_slate_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    assays = [
        {'Code': 'AGBMI472', 'Library': 'CHEVRON_EQUITY', 'Selected': 'true',},
        {'Code': 'AGBMI480', 'Library': 'CHEVRON_EQUITY', 'Selected': 'true',}
    ]
    template = {
        "SlateItems": assays,
        "Name": slate_name
    }
    return template


def test_post_slate():
    template = get_slate_template()
    res = slates.post_slate(template)
    assert res == 'Created'
    time.sleep(1)
    testslate = slates.get_slate_by_name(template["Name"])
    res = slates.delete_slate(testslate['ID'].iloc[0])
    assert res == 'No Content'
