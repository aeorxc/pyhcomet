from pyhcomet import blends
import pandas as pd
import time


def test_get_blends():
    res = blends.get_blends()
    assert res is not None
    if len(res) > 0:
        id = res['ID'].iloc[0]
        res = blends.get_blend(id)
        assert res is not None

def test_get_blend():
    res = blends.get_blend(44999)
    assert res is not None

def test_build_slate_template():
    crudes = [
        {
            "Percent": 50,
            "Code": "AGBMI472",
            "Library": "CHEVRON_EQUITY",
        },
        {
            "Percent": 50,
            "Code": "AGBMI480",
            "Library": "CHEVRON_EQUITY",
        },
    ]
    res = blends.blend_template(crudes, "test_slate")
    assert res is not None

def get_blend_template():
    slate_name = (
        f"test_blend_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    )
    assays = [
        {
            "Percent": 50,
            "Code": "AGBMI472",
            "Library": "CHEVRON_EQUITY",
        },
        {
            "Percent": 50,
            "Code": "AGBMI480",
            "Library": "CHEVRON_EQUITY",
        },
    ]
    template = blends.blend_template(assays, name=slate_name)
    return template

def test_post_blend():
    template = get_blend_template()
    res = blends.post_blend(template)
    assert res == "Created"
    time.sleep(1)
    testblend = blends.get_blend_by_name(template["Name"])
    res = blends.delete_blend(testblend["ID"].iloc[0])
    assert res == "No Content"
