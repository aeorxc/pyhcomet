import requests
import pandas as pd
from pyhcomet import hcometcore
import json
api_url = "https://hcomet.haverly.com/api/slates"

def get_slates():
    payload = {}
    try:
        response = requests.request("GET", api_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def get_slate(slate_id: int):
    set_url = f"{api_url}/{slate_id}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame(d.items())
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def post_slate(slate: dict):
    payload = json.dumps(slate)
    try:
        response = requests.request("GET", api_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 201:
            d = response.json()
            return d
    except:
        return "Error: no response.  Was the url correct?\n"