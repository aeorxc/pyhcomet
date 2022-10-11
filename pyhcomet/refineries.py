import requests
import pandas as pd
from pyhcomet import hcometcore
import json

api_url = "https://hcomet.haverly.com/api/basref"

def get_refinary_list(region_id: str, country: str):
    set_url = f"{api_url}/sys?regionID={region_id}&country={country}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def get_refinary(region_id: str, refinary_id: int):
    set_url = f"{api_url}/sys/{region_id}/{refinary_id}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame(d.items())
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def get_units_template():
    set_url = f"{api_url}/units"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def get_refinary_configs(region_id: str):
    set_url = f"{api_url}/config/{region_id}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def get_refinary_config(region_id: str, config_id: int):
    set_url = f"{api_url}/config/{region_id}/{config_id}"
    payload = {}
    try:
        response = requests.request("GET", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"

def post_refinary_config(region_id: str, config: dict):
    set_url = f"{api_url}/config/{region_id}"
    payload = json.dumps(config)
    try:
        response = requests.request("POST", set_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 201:
            d = response.json()
            return d
    except:
        return "Error: no response.  Was the url correct?\n"