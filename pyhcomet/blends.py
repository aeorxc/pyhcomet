import requests
import pandas as pd
from pyhcomet import hcometcore
import json
api_url = "https://hcomet.haverly.com/api/blends"

def get_blends():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_records(d)
    return df

def get_blend(blend_id: int):
    set_url = f"{api_url}/{blend_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df

def post_blend(blend: dict):
    payload = json.dumps(blend)
    d = hcometcore.generic_api_call(api_url, payload=payload, requestType="POST", response_code=201)
    return d

print(get_blend(44999))