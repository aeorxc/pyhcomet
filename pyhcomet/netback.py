import logging

import requests
import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/basnb"


def run_netback_case(case_id:int) -> int:
    """
    Given a case_id run netback model. Returns the nbIndex for a case
    :param case_id:
    :return:
    """

    case_url = f"{api_url}/{case_id}"
    try:
        response = requests.post(case_url, headers=hcometcore.get_header(), data={})
        if response.status_code == 201:
            return response.json()['nbIndex']
        if response.status_code == 500:
            logging.warning(response.json()['Message'])
    except:
        return "Error: no response.  Was the url correct?\n"


def get_run_status(nbIndex:int):
    run_status_url = f"{api_url}/status/{nbIndex}"
    d = hcometcore.generic_api_call(run_status_url)
    return d

def get_report(nbIndex:int, rateType:int=0, report_type:str='reportnb') -> list:
    report_url = f"{api_url}/{report_type}/{nbIndex}/{rateType}"
    d = hcometcore.generic_api_call(report_url)
    return d