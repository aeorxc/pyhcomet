import pandas as pd
from pyhcomet import hcometcore
import json
from qe import qe

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
    d = hcometcore.generic_api_call(set_url, payload=payload, requestType="POST", response_code=201, convert='true')
    return d

def get_ref_config(region: str, name: str):
    listofrefsinregions = get_refinary_configs(region)
    configID= int(listofrefsinregions.query('Name == @name')['ID'].iloc[0])
    return configID

def put_refinary_config(config: dict, region_id: str, configID: int):
    set_url = f"{api_url}/config/{region_id}/{configID}"
    payload = json.dumps(config)
    d = hcometcore.generic_api_call(set_url, payload=payload, requestType="PUT", response_code=204, convert='true')
    return d

def delete_config(region_id: str, config_id: int):
    set_url = f"{api_url}/config/{region_id}/{config_id}"
    d = hcometcore.generic_api_call(set_url, payload={}, requestType="DELETE", response_code=204, convert='true')
    return d

def get_refinary_id_on_country(region_id: str, country: str, type: str):
    x = get_refinary_list(region_id,country)
    refid = int(x.query('Name == @type')['ID'].iloc[0])
    return refid