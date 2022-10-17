import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/regions"


def get_regions():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_records(d)
    return df
