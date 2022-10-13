import requests
import pandas as pd
from pyhcomet import hcometcore
import json
api_url = "https://hcomet.haverly.com/api/slates"

def get_slates():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_dict(d)
    return df

def get_slate(slate_id: int):
    set_url = f"{api_url}/{slate_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df

def post_slate(slate: dict):
    payload = json.dumps(slate)
    d = hcometcore.generic_api_call(api_url, payload=payload, requestType="POST", response_code=201, convert='true')
    return d

def get_slate_id(name: str):
    listofslates = get_slates()
    ID= int(listofslates.query('Name == @name')['ID'].iloc[0])
    return ID
