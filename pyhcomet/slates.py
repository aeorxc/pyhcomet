import json

import pandas as pd

from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/slates"


def slate_template(crudes: list, name: str):
    """
    Given a list of dicts (eg below) construct a template to send to Haverly
    crudes = [
        {'Code': 'AGBMI472', 'Library': 'CHEVRON_EQUITY',  },
        {'Code': 'AGBMI480', 'Library': 'CHEVRON_EQUITY', }
    ]
    :param crudes:
    :param name:
    :return:
    """

    template = {
        "SlateItems": [],
        "Name": name
    }
    for crude in crudes:
        t = {'Selected': 'true'}
        t = {**crude, **t}
        template["SlateItems"].append(t)

    return template


def get_slates():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_dict(d)
    return df


def get_slate(slate_id: int):
    set_url = f"{api_url}/{slate_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df


def get_slate_by_name(slate_name: int):
    slates = get_slates()
    slates = slates[slates['Name'] == slate_name]
    if len(slates) > 0:
        return slates


def post_slate(slate: dict):
    """
    Given a Slate template create a new slate
    :param slate: Dict of format "{"SlateItems": ["AssayCode1", "AssayCode2"], "Name": "slate_name"}"
    :return:
    """
    payload = json.dumps(slate)
    d = hcometcore.generic_api_call(api_url, payload=payload, requestType="POST", response_code=201, convert='true')
    return d.reason


def get_slate_id(name: str):
    listofslates = get_slates()
    ID = int(listofslates.query('Name == @name')['ID'].iloc[0])
    return ID


def put_slate(slate_id: int, slate: dict):
    set_url = f"{api_url}/{slate_id}"
    payload = json.dumps(slate)
    d = hcometcore.generic_api_call(set_url, payload=payload, requestType="PUT", response_code=204, convert='true')
    return d


def delete_slate(slate_id: int):
    set_url = f"{api_url}/{slate_id}"
    d = hcometcore.generic_api_call(set_url, payload={}, requestType="DELETE", response_code=204, convert='true')
    return d.reason
