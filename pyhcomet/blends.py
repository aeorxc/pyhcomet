import pandas as pd
from pyhcomet import hcometcore
import json

api_url = "https://hcomet.haverly.com/api/blends"


def get_blends():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_records(d)
    return df


def get_blend(blend_id: int):
    set_url = f"{api_url}/{blend_id}"
    d = hcometcore.generic_api_call(set_url)
    df = pd.DataFrame(d.items())
    return df


def post_blend(blend: dict):
    payload = json.dumps(blend)
    d = hcometcore.generic_api_call(
        api_url,
        payload=payload,
        requestType="POST",
        expected_response_code=201,
        convert="true",
    )
    return d.reason


def put_blend(blend_id: int, blend: dict):
    set_url = f"{api_url}/{blend_id}"
    payload = json.dumps(blend)
    d = hcometcore.generic_api_call(
        set_url,
        payload=payload,
        requestType="PUT",
        expected_response_code=204,
        convert="true",
    )
    return d.reason


def delete_blend(blend_id: int):
    set_url = f"{api_url}/{blend_id}"
    d = hcometcore.generic_api_call(
        set_url,
        payload={},
        requestType="DELETE",
        expected_response_code=204,
        convert="true",
    )
    return d.reason


def blend_template(crudes: list, name: str):
    """
    Given a list of dicts (eg below) construct a template to send to Haverly
    crudes = [
        {'Percent': 50, 'Code': 'AGBMI472', 'Library': 'CHEVRON_EQUITY',  },
        {'Percent: 50, ''Code': 'AGBMI480', 'Library': 'CHEVRON_EQUITY', }
    ]
    :param crudes:
    :param name:
    :return:
    """

    template = {"BlendComponentCrudes": [], "Name": name}
    for crude in crudes:
        t = {"Selected": "true"}
        t = {**crude, **t}
        template["BlendComponentCrudes"].append(t)

    return template


def get_blend_by_name(blend_name: str):
    blends = get_blends()
    blends = blends[blends["Name"] == blend_name]
    if len(blends) > 0:
        return blends
