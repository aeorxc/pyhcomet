from pyhcomet import slates
from pyhcomet import create_slate
import pandas as pd
import pytest

def test_get_slates():
    res = slates.get_slates()
    assert res is not None

def test_get_slate():
    res = slates.get_slate(25458)
    assert res is not None


def test_post_slate():
    slate_name = pd.to_datetime('now').strftime('%y%m%d%I%M%S')
    assays = ["Agbami '07", "Agbami (GSC) July '18", "Agbami (CVX) Mar 16 '21"]
    template = {
        "SlateItems": assays,
        "Name": slate_name
    }
    res = slates.post_slate(template)
    assert res == 'Created'
    allslates = slates.get_slates()
    testslate = allslates[allslates['Name'] == slate_name]
    slates.delete_slate(testslate['ID'].iloc[0])