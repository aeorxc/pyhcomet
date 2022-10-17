import json

import pandas as pd

from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/cases"


def case_template(SimplePriceSetID: int,
                  RegionID: str,
                  Name: str,
                  SlateID: int = None,
                  BlendID: int = None,
                  SimpleRefineryConfigID: int = 72193 # NWE Generic
    ):
    template = {
        'Selected': True,
        'SlateOrBlend': '',
        'SlateID': "" if SlateID is None else int(SlateID),
        'BlendID': "" if BlendID is None else int(BlendID),
        'CutSetID': None,
        'ModelType': 0,
        'RegionID': RegionID,
        'PriceSetType': 0,
        'SimplePriceSetID': int(SimplePriceSetID),
        'SimplePriceSetGroupID': None,
        'SimpleRefineryConfigID': SimpleRefineryConfigID,
        'SimpleSpecificationID': 1884,
        'SimpleCutSetID': 0,
        'SimpleSeasonCode': 'INT',
        'Name': Name
    }
    return template


def get_cases():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_dict(d)
    return df


def get_case(case_id: int):
    set_url = f"{api_url}/{case_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df


def get_case_by_name(case_name: str):
    cases = get_cases()
    cases = cases[cases['Name'] == case_name]
    if len(cases) > 0:
        return cases


def post_case(case: dict):
    payload = json.dumps(case)
    d = hcometcore.generic_api_call(api_url, payload=payload, requestType="POST", response_code=201, convert='true')
    return d.reason


def put_case(case_id: int, case: dict):
    set_url = f"{api_url}/{case_id}"
    payload = json.dumps(case)
    d = hcometcore.generic_api_call(set_url, payload=payload, requestType="PUT", response_code=204, convert='true')
    return d


def delete_case(case_id: int):
    set_url = f"{api_url}/{case_id}"
    d = hcometcore.generic_api_call(set_url, payload={}, requestType="DELETE", response_code=204, convert='true')
    return d.reason
