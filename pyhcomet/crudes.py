import pandas as pd
from pyhcomet import hcometcore

api_url = "https://hcomet.haverly.com/api/crudes"


def get_crudes():
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_dict(d)
    return df


def extract_cut_properties(cut):
    p = pd.DataFrame(cut.Properties)
    p['Name'] = cut.Name
    return p

def get_crude(name: str, assay_format: str = "english assay"):
    crude_url = f"{api_url}/comet/{name}/{assay_format}"
    d = hcometcore.generic_api_call(crude_url)
    res = pd.DataFrame(pd.Series(d))
    res.attrs['summaryProperties'] = pd.DataFrame(d["summaryProperties"])
    res.attrs['WCProperties'] = pd.DataFrame(d["WCProperties"])
    Cuts = pd.DataFrame(d["Cuts"])
    CutsProperties = pd.concat(Cuts.apply(lambda x: extract_cut_properties(x), 1).values, axis=0)
    res.attrs['Cuts'] = Cuts
    res.attrs['CutsProperties'] = CutsProperties

    return res


def get_crude_library():
    crude_url = f"{api_url}/crulib/library"
    d = hcometcore.generic_api_call(crude_url)
    return d
