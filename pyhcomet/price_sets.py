import requests
import pandas as pd
from pyhcomet import hcometcore
import json

api_url = "https://hcomet.haverly.com/api/cpss"

def get_price_sets(region_id: str):
    set_url = f"{api_url}/{region_id}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def get_price_set(set_id: int):
    set_url = f"{api_url}/{set_id}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.Series(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def post_crude_price(price_set, region_id: str):
    set_url = f"{api_url}/{region_id}"
    payload = json.dumps(price_set)
    try:
        response = requests.request("POST", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 201:
            return response
    except:
        return "Error: no response.  Was the url correct?\n"