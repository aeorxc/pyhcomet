import logging
import time

import pandas as pd

from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/basnb"


def run_netback_case(case_id: int) -> int:
    """
    Given a case_id run netback model. Returns the nbIndex for a case
    :param case_id:
    :return:
    """

    case_url = f"{api_url}/{case_id}"
    d = hcometcore.generic_api_call(
        case_url, payload={}, requestType="POST", response_code=201, convert="true"
    )
    return d.json()["nbIndex"]


def run_case_and_get_report(case_id: int) -> dict:
    nbID = run_netback_case(case_id)
    while get_run_status(nbID)[0] != "complete":
        state = get_run_status(nbID)
        logging.info(f"State of case id: {case_id} is {state}, check update in 5 secs")
        time.sleep(5)
    report = get_report(nbID)
    products = report.loc["Products"][0]
    products = pd.DataFrame(products)
    return products


def get_run_status(nbIndex: int):
    run_status_url = f"{api_url}/status/{nbIndex}"
    d = hcometcore.generic_api_call(run_status_url)
    return d


def get_report(nbIndex: int, rateType: int = 0, report_type: str = "reportnb") -> list:
    report_url = f"{api_url}/{report_type}/{nbIndex}/{rateType}"
    d = hcometcore.generic_api_call(report_url)
    d = pd.DataFrame.from_records(d).T
    return d
