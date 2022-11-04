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
    crudes = [{'Code': 'SAHB2013', 'Library': 'COMET'},
 {'Code': 'SURURU2020', 'Library': 'COMET'},
 {'Code': 'UTFBT085', 'Library': 'CHEVRON_EQUITY'},
 {'Code': 'LIZA216', 'Library': 'COMET'},
 {'Code': 'BasrahMedium2021', 'Library': 'COMET'},
 {'Code': 'SARIR2007', 'Library': 'COMET'},
 {'Code': 'ISTHMUS2005', 'Library': 'COMET'},
 {'Code': 'JOHANSVERD2021', 'Library': 'COMET'},
 {'Code': 'URALS_PRIMORSK2005', 'Library': 'COMET'},
 {'Code': 'BASHKIRI2003', 'Library': 'COMET'},
 {'Code': 'SIBERIANLIGHT2004', 'Library': 'COMET'},
 {'Code': 'BEZENT2005', 'Library': 'COMET'},
 {'Code': 'ARABHV2012', 'Library': 'COMET'},
 {'Code': 'ArabLt2018', 'Library': 'COMET'},
 {'Code': 'STEXS326', 'Library': 'COMET'},
 {'Code': 'GRNCN301', 'Library': 'CHEVRON_EQUITY'},
 {'Code': 'WTXLT462a', 'Library': 'CHEVRON_EQUITY'}]
    name = f"test_slate_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"

    set_id = slates.submit_slate(crudes=crudes, name=name)
    assert set_id is not None
    time.sleep(1)
    res = slates.delete_slate(set_id)
    assert res == "No Content"
