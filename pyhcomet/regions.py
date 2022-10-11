import requests
import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/regions"

def get_regions():
    payload = {}
    try:
        response = requests.request("GET", api_url, headers=hcometcore.get_header(), data=payload)
        if response.status_code == 200:
            d = response.json()
            df = pd.DataFrame.from_records(d)
            return df
    except:
        return "Error: no response.  Was the url correct?\n"