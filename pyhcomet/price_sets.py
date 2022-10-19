import json

import pandas as pd

from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/baspss"

product_defaults = {
    "Selected": "true",
    "RateUnit": "Vol%",
    "Type": 0,
}

product_template_defaults = {
    "LPG": {"Code": "LPG", "Description": "LPG", "LPCode": "LPG"},
    "Naphtha": {"Code": "LNA", "Description": "Naphtha", "LPCode": "LNA"},
    "Mogas Prem 95": {
        "Code": "MOGHQ",
        "Description": "Mogas Prem 95",
        "LPCode": "MGH",
    },
    "Mogas Reg 92": {
        "Code": "MOGLQ",
        "Description": "Mogas Reg 92",
        "LPCode": "MGL",
    },
    "Jet-A1": {"Code": "JET", "Description": "Jet-A1", "LPCode": "JET"},
    "Diesel 10ppm S": {
        "Code": "DIEHQ",
        "Description": "Diesel 10ppm S",
        "LPCode": "DSH",
    },
    "Diesel 50ppm S": {
        "Code": "DIELQ",
        "Description": "Diesel 50ppm S",
        "LPCode": "DSL",
    },
    "Heating Oil 0.1% S": {
        "Code": "HOLHQ",
        "Description": "Heating Oil 0.1% S",
        "LPCode": "HOH",
    },
    "Heating Oil 0.2% S": {
        "Code": "HOLLQ",
        "Description": "Heating Oil 0.2% S",
        "LPCode": "HOL",
    },
    "Fuel Oil 0.5% S": {
        "Code": "FOULS",
        "Description": "Fuel Oil 0.5% S",
        "LPCode": "FUS",
    },
    "Fuel Oil 1% S": {
        "Code": "FOLHQ",
        "Description": "Fuel Oil 1% S",
        "LPCode": "FOH",
    },
    "Fuel Oil 3.5% S": {
        "Code": "FOLLQ",
        "Description": "Fuel Oil 3.5% S",
        "LPCode": "FOL",
    },
    "Bitumen": {"Code": "ASP", "Description": "Bitumen", "LPCode": "ASP"},
}


def price_set_template(prices: list, name: str) -> dict:
    """
    Given a list of dicts (eg below) construct a template to send to Haverly
    [
        {
            "Description": "LPG",
            "Price": 650,
            "PriceUnit": '$/MT'
        },
    ]
    :param prices:
    :param name:
    :return:
    """
    t = {"Name": name, "Products": []}
    count = 1
    for price in prices:
        product = {**price, **product_defaults}  # add in prices
        product = {
            **product_template_defaults[price["Description"]],
            **product,
        }  # add in other defaults
        product["Number"] = count
        t["Products"].append(product)
        count += 1

    return t


def get_price_sets(region_id: str):
    set_url = f"{api_url}/{region_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame.from_records(d)
    return df


def get_price_set(region_id: str, set_id: int):
    set_url = f"{api_url}/{region_id}/{set_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.Series(d)
    return df


def get_price_set_by_name(region_id: str, set_name: str):
    sets = get_price_sets(region_id)
    sets = sets[sets["Name"] == set_name]
    if len(sets) > 0:
        return sets


def post_price_set(price_set: dict, region_id: str):
    set_url = f"{api_url}/{region_id}"
    payload = json.dumps(price_set)
    d = hcometcore.generic_api_call(
        set_url,
        payload=payload,
        requestType="POST",
        expected_response_code=201,
        convert="true",
    )
    return d.reason


def get_price_set_id(region: str, name: str):
    listofsets = get_price_sets(region)
    ID = int(listofsets.query("Name == @name")["ID"].iloc[0])
    return ID


def put_price_set(region_id: str, price_set_id: int, price_set: dict):
    set_url = f"{api_url}/{region_id}/{price_set_id}"
    payload = json.dumps(price_set)
    d = hcometcore.generic_api_call(
        set_url,
        payload=payload,
        requestType="PUT",
        expected_response_code=204,
        convert="true",
    )
    return d


def delete_set(region_id: str, set_id: int):
    set_url = f"{api_url}/{region_id}/{set_id}"
    d = hcometcore.generic_api_call(
        set_url,
        payload={},
        requestType="DELETE",
        expected_response_code=204,
        convert="true",
    )
    return d.reason


def submit_price_set(prices: list, region_id: str, name: str):
    """
    Given a list of dicts (eg below) construct a template and send to Haverly.
    If a set exists with supplied name, overwrite
    [
        {
            "Description": "LPG",
            "Price": 650,
            "PriceUnit": '$/MT'
        },
    ]
    :param prices:
    :param region_id:
    :param name:
    :return:
    """
    template = price_set_template(prices=prices, name=name)
    set_id = None
    try:
        post_price_set(price_set=template, region_id=region_id)
    except Exception as ex:
        if "Basic price set name conflict" in ex.reason:
            set_id = get_price_set_by_name(region_id=region_id, set_name=name)[
                "ID"
            ].iloc[0]
            put_price_set(region_id=region_id, price_set=template, price_set_id=set_id)
        else:
            raise

    if not set_id:
        set_id = get_price_set_by_name(region_id=region_id, set_name=name)["ID"].iloc[0]

    return set_id


if __name__ == "__main__":
    prices = [
        {"Description": "LPG", "Price": 650, "PriceUnit": "$/MT"},
        {"Description": "Naphtha", "Price": 750, "PriceUnit": "$/MT"},
    ]
    submit_price_set(prices=prices, region_id="NWE", name="ga_test")
