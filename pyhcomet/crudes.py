import requests
import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/crudes"


def get_crude(name:str, assay_format:str = "english assay"):
    payload = {}

    crude_url = f"{api_url}/comet/{name}/{assay_format}"
    try:
        response = requests.request("GET", crude_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            res = pd.DataFrame(d['summaryProperties']) # TODO read rest of response
            return res
    except:
        return "Error: no response.  Was the url correct?\n"

