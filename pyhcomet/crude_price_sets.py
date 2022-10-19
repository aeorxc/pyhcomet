import pandas as pd
from pyhcomet import hcometcore
import json

api_url = "https://hcomet.haverly.com/api/cpss"


def get_crude_price_sets(region_id: str):
    set_url = f"{api_url}/{region_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame.from_records(d)
    return df


def get_crude_price_set(set_id: int):
    set_url = f"{api_url}/{set_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.Series(d)
    return df


def post_crude_price_set(price_set, region_id: str):
    set_url = f"{api_url}/{region_id}"
    payload = json.dumps(price_set)
    d = hcometcore.generic_api_call(
        set_url,
        payload=payload,
        requestType="POST",
        expected_response_code=201,
        convert="true",
    )
    return d
