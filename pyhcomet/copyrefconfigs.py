import refineries
from pyhcomet import hcometcore
import pandas as pd


def create_configs():
    api_url = "https://hcomet.haverly.com/api/regions"
    d = hcometcore.generic_api_call(api_url)
    df = pd.DataFrame.from_dict(d)
    regions = df["ID"].to_list()

    for region in regions:
        api_url = f"https://hcomet.haverly.com/api/countries/{region}"
        d = hcometcore.generic_api_call(api_url)
        df = pd.DataFrame.from_dict(d)
        countries = df["Name"].to_list()

        for country in countries:
            x = refineries.get_refinary_list(region, country)

            x = x[["ID", "Name"]]
            x = dict(zip(x.Name, x.ID))

            for name, value in x.items():
                template = refineries.get_refinary("NWE", value)
                template = template.iloc[0][1]

                reftemp = {
                    "Refineries": [
                        {
                            "Units": template,
                            "ID": 1,
                            "Name": name,
                            "Selected": "true",
                            "IsSelected": "true",
                            "SelectedRefineriesCount": 1,
                            "Name": name,
                        }
                    ],
                    "Name": name,
                }
                try:
                    y = refineries.get_refinary_configs(region)
                    configid = int(y.query("Name == @name")["ID"].iloc[0])
                    print(configid)
                    continue
                except:
                    refineries.post_refinary_config(reftemp, region)
                    y = refineries.get_refinary_configs(region)
                    configid = int(y.query("Name == @name")["ID"].iloc[0])
                    print(configid)
                    print(region)
                    print(country)


create_configs()
