import json

import pandas as pd

from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/baspss"


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


def post_price_set(price_set: dict, region_id: str):
    set_url = f"{api_url}/{region_id}"
    payload = json.dumps(price_set)
    d = hcometcore.generic_api_call(set_url, payload=payload, requestType="POST", response_code=201, convert='true')
    return d.reason


def get_price_set_id(region: str, name: str):
    listofsets = get_price_sets(region)
    ID = int(listofsets.query('Name == @name')['ID'].iloc[0])
    return ID


def put_price_set(region_id: str, price_set_id: int, price_set: dict):
    set_url = f"{api_url}/{region_id}/{price_set_id}"
    payload = json.dumps(price_set)
    d = hcometcore.generic_api_call(set_url, payload=payload, requestType="PUT", response_code=204, convert='true')
    return d


def delete_set(region_id: str, set_id: int):
    set_url = f"{api_url}/{region_id}/{set_id}"
    d = hcometcore.generic_api_call(set_url, payload={}, requestType="DELETE", response_code=204, convert='true')
    return d.reason
