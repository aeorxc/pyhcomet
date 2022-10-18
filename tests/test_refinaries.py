from pyhcomet import refineries
import pandas as pd
import time


def test_get_refinary_list():
    res = refineries.get_refinary_list("NWE", "GERMANY")
    assert res is not None

def test_get_refinary():
    res = refineries.get_refinary("NWE", 72687)
    assert res is not None

def test_get_units_template():
    res = refineries.get_units_template()
    assert res is not None

def test_get_refinary_configs():
    res = refineries.get_refinary_configs("NWE")
    assert res is not None
    if len(res) > 0:
        id = res["ID"].iloc[0]
        res = refineries.get_refinary_config("NWE", id)
        assert res is not None

def test_get_refinary_config():
    res = refineries.get_refinary_config('NWE', 73837)
    assert res is not None

def test_get_ref_config():
    res = refineries.get_ref_config('NWE', 'ABNynas_Harburg')
    assert res is not None

def test_get_ref_id():
    res = refineries.get_refinary_id_on_country('NWE','GERMANY','ABNynas_Harburg')
    assert res is not None

def test_build_ref_template():
    ref = [
        {
            'Code': 'ADU',
            'Name': 'Atm. Dist. Unit',
            'Capacity': 20000,
        },
        {
            'Code': 'ALK',
            'Name': 'Alkylation',
            'Capacity': 15000,
        },
    ]
    res = refineries.ref_template(ref, "test_ref")
    assert res is not None

def get_ref_template():
    ref_name = (
        f"test_blend_{pd.to_datetime('now', utc=True).strftime('%y%m%d%I%M%S')}"
    )
    ref = [
        {
            'Code': 'ADU',
            'Name': 'Atm. Dist. Unit',
            'Capacity': 20000,
        },
        {
            'Code': 'ALK',
            'Name': 'Alkylation',
            'Capacity': 15000,
        },
    ]
    template = refineries.ref_template(ref, name=ref_name)
    return template

def test_post_ref():
    template = get_ref_template()
    res = refineries.post_refinary_config(template, 'NWE')
    assert res == "Created"
    time.sleep(1)
    testref = refineries.get_ref_config('NWE',template["Name"])
    res = refineries.delete_config('NWE', testref)
    assert res == "No Content"
