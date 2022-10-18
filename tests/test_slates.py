import time

import pandas as pd

from pyhcomet import slates


def test_get_slates():
    res = slates.get_slates()
    assert res is not None
    if len(res) > 0:
        id = res["ID"].iloc[0]
        res = slates.get_slate(id)
        assert res is not None


def get_slate_template():
    slate_name = (

    )
    assays = [
        {
            "Code": "AGBMI472",
            "Library": "CHEVRON_EQUITY",
        },
        {
            "Code": "AGBMI480",
            "Library": "CHEVRON_EQUITY",
        },
    ]
    template = slates.slate_template(assays, name=slate_name)
    return template


def test_submit_slate():
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

    set_id = slates.submit_slate(crudes=crudes, name=name)
    assert set_id is not None
    time.sleep(1)
    res = slates.delete_slate(set_id)
    assert res == "No Content"
