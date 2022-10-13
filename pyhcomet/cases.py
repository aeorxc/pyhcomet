import pandas as pd
from pyhcomet import hcometcore
import json

api_url = "https://hcomet.haverly.com/api/cases"


def get_cases():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_dict(d)
    return df

def get_case(case_id: int):
    set_url = f"{api_url}/{case_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df


def post_case(case: dict):
    payload = json.dumps(case)
    d = hcometcore.generic_api_call(api_url, payload=payload, requestType="POST", response_code=201, convert='true')
    return d
