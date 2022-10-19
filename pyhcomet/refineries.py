import json

import pandas as pd

from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/basref"


def get_refinary_list(region_id: str, country: str):
    set_url = f"{api_url}/sys?regionID={region_id}&country={country}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame.from_records(d)
    return df


def get_refinary(region_id: str, refinary_id: int):
    set_url = f"{api_url}/sys/{region_id}/{refinary_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df


def get_units_template():
    set_url = f"{api_url}/units"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame.from_records(d)
    return df


def get_refinary_configs(region_id: str):
    set_url = f"{api_url}/config/{region_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame.from_records(d)
    return df


def get_refinary_config(region_id: str, config_id: int):
    set_url = f"{api_url}/config/{region_id}/{config_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame.from_records(d)
    return df


def post_refinary_config(config: dict, region_id: str):
    set_url = f"{api_url}/config/{region_id}"
    payload = json.dumps(config)
    d = hcometcore.generic_api_call(
        set_url,
        payload=payload,
        requestType="POST",
        expected_response_code=201,
        convert="true",
    )
    return d.reason


def get_ref_config(region: str, name: str):
    listofrefsinregions = get_refinary_configs(region)
    configID = int(listofrefsinregions.query("Name == @name")["ID"].iloc[0])
    return configID


def put_refinary_config(config: dict, region_id: str, configID: int):
    set_url = f"{api_url}/config/{region_id}/{configID}"
    payload = json.dumps(config)
    d = hcometcore.generic_api_call(
        set_url,
        payload=payload,
        requestType="PUT",
        expected_response_code=204,
        convert="true",
    )
    return d.reason


def delete_config(region_id: str, config_id: int):
    set_url = f"{api_url}/config/{region_id}/{config_id}"
    d = hcometcore.generic_api_call(
        set_url,
        payload={},
        requestType="DELETE",
        expected_response_code=204,
        convert="true",
    )
    return d.reason


def get_refinary_id_on_country(region_id: str, country: str, name: str):
    x = get_refinary_list(region_id, country)
    refid = int(x.query("Name == @name")["ID"].iloc[0])
    return refid


def ref_template(units: list, name: str):
    """
    Given a list of dicts (eg below) construct a template to send to Haverly
    units = [
        {'Code': 'ADU', 'Name': 'Atm. Dist. Unit', 'Capacity': 20000,},
        {'Code': 'ALK', 'Name': 'Alkylation', 'Capacity': 15000,}
    ]
    :param units:
    :param name:
    :return:
    """

    template = {
        "Units": [],
        "ID": 1,
        "Name": name,
        "Selected": "true",
        "IsSelected": "true",
        "SelectedRefineriesCount": 1,
        "Name": name,
    }
    for unit in units:
        t = {"Selected": "true", "Enabled": "true", "Rate": "null", "MinRate": "null"}
        t = {**unit, **t}
        template["Units"].append(t)
    template = {"Refineries": [template], "Name": name}
    return template
