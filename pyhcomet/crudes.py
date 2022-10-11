import requests
import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/crudes"


def get_crude(name:str, assay_format:str = "english assay"):
    crude_url = f"{api_url}/comet/{name}/{assay_format}"
    d = hcometcore.generic_api_call(crude_url)
    res = pd.DataFrame(d['summaryProperties']) #TODO read rest of response
    return res


def get_crudes():
    d = hcometcore.generic_api_call(api_url)
    res = pd.DataFrame(d)
    return res

def get_crude_library():
    crude_url = f"{api_url}/crulib/library"
    d = hcometcore.generic_api_call(crude_url)
    res = 1
    return res
