import requests
import pandas as pd
from pyhcomet import hcometcore
import json

api_url = "https://hcomet.haverly.com/api/cases"

def get_cases():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame([pd.Series(d[0]) for x in d])
    return df

def get_case(id:int):
    set_url = f"{api_url}/{id}"
    d = hcometcore.generic_api_call(set_url)
    return pd.Series(d)

def post_case(case: dict):
    payload = json.dumps(case)
    d = hcometcore.generic_api_call(api_url, payload=payload, requestType="POST", response_code=201)
    return d