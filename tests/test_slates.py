import pandas as pd
import time
from pyhcomet import slates


def test_get_slates():
    res = slates.get_slates()
    assert res is not None


def test_get_slate():
    res = slates.get_slate(25458)
    assert res is not None


def test_post_slate():
    slate_name = f"test_slate_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    assays = ["Agbami '07", "Agbami (GSC) July '18"]
    template = {
        "SlateItems": assays,
        "Name": slate_name
    }
    res = slates.post_slate(template)
    assert res == 'Created'
    time.sleep(1)
    allslates = slates.get_slates()
    testslate = allslates[allslates['Name'] == slate_name]
    res = slates.delete_slate(testslate['ID'].iloc[0])
    assert res == 'No Content'
