import requests
import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/cases"


def get_cases():
    payload = {}
    try:
        response = requests.request("GET", api_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame([pd.Series(d[0]) for x in d])
            return df
    except:
        return "Error: no response.  Was the url correct?\n"


def get_case(id:int):
    payload = {}
    case_url = f"{api_url}/{id}"
    try:
        response = requests.request("GET", case_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            return pd.Series(d)
    except:
        return "Error: no response.  Was the url correct?\n"