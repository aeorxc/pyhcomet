from pyhcomet import refineries


def test_get_refinary_list():
    res = refineries.get_refinary_list("NWE", "GERMANY")
    assert res is not None


def test_get_refinary():
    res = refineries.get_refinary("NWE", 72687)
    assert res is not None


def test_get_refinary_configs():
    res = refineries.get_refinary_configs("NWE")
    assert res is not None
    if len(res) > 0:
        id = res["ID"].iloc[0]
        res = refineries.get_refinary_config("NWE", id)
        assert res is not None
