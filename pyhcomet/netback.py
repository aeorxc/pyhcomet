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
        case_url,
        payload={},
        requestType="POST",
        expected_response_code=201,
        convert="true",
    )
    return d.json()["nbIndex"]


def run_case_and_get_report(case_id: int, rateType: int = 1) -> dict:
    nbID = run_netback_case(case_id)
    while get_run_status(nbID)[0] != "complete":
        state = get_run_status(nbID)
        logging.info(f"State of case id: {case_id} is {state}, check update in 5 secs")
        time.sleep(5)
    report = get_report(nbID, rateType=rateType)
    return report


def get_run_status(nbIndex: int):
    run_status_url = f"{api_url}/status/{nbIndex}"
    d = hcometcore.generic_api_call(run_status_url)
    return d


def get_report(nbIndex: int, rateType: int = 1, report_type: str = "reportnb") -> list:
    report_url = f"{api_url}/{report_type}/{nbIndex}/{rateType}"
    d = hcometcore.generic_api_call(report_url)
    df = pd.DataFrame.from_records(d).T
    df = extract_sub_reports(df)
    return df


def extract_sub_reports(df):
    """Given a netback report extract the subreports in put into df.attrs"""
    # df contains nested dataframes - put these into the df.attrs section for easier access
    for subreport in ["FeedStocks", "Products", "UnUsedStreams"]:
        subreport_df = [pd.DataFrame(x) for x in df.loc[subreport]]
        # add in these columns from the initial report (df) into the sub reports
        crudeIndex = df.loc[
            ["CrudeIndex", "PriceSetName", "CrudeCode", "CrudeName", "CrudeLibrary"]
        ]
        for i in range(0, len(df.columns)):
            d = subreport_df[i]
            e = (
                pd.DataFrame(crudeIndex[i])
                .T.reset_index()
                .reindex(d.index)
                .fillna(method="ffill")
            )
            subreport_df[i] = pd.concat([d, e], axis=1)
        subreport_df = pd.concat(subreport_df, axis=0)
        df.attrs[subreport] = subreport_df

    return df
