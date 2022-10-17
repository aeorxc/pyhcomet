import cases
import create_slate
import create_price_set
import refineries
import create_blend

def create_template(assays: list, percent: dict, region: str, productPrices: dict, Units: dict, name: str, slateorblend: int, type: str, codes: dict, seasonCode: str):
    settings = {'SlateID': create_slate.create_and_post_slate(assays, name), 'BlendID': create_blend.create_and_post_blend(assays, percent, name), 'RegionID': region,
                'SimplePriceSetID': create_price_set.create_and_post_price_set(productPrices,
                                  Units, name, region, codes),
                'SimpleRefineryConfigID': refineries.get_ref_config(region, type),
                'SimpleSeasonCode': seasonCode, 'SimpleCutSetID': 0, 'SimpleSpecificationID': 1884}

    casetemplate = {'Selected': True, 'SlateOrBlend': slateorblend, 'SlateID': settings['SlateID'],
                    'BlendID': settings['BlendID'], 'ModelType': 0, 'RegionID': settings['RegionID'],
                    'PriceSetType': 0, 'SimplePriceSetID': settings['SimplePriceSetID'], 'SimplePriceSetGroupID': None,
                    'SimpleRefineryConfigID': settings['SimpleRefineryConfigID'],
                    'SimpleSpecificationID': settings['SimpleSpecificationID'],
                    'SimpleCutSetID': settings['SimpleCutSetID'], 'SimpleSeasonCode': settings['SimpleSeasonCode'], 'Name': name}
    return casetemplate

def create_and_post_case(assays: list, percent: dict, region: str, productPrices: dict, Units: dict, name: str, slateorblend: int, type: str, codes: dict, seasonCode: str):
    x = cases.get_cases()
    try:
        caseid = int(x.query('Name == @name')['ID'].iloc[0])
        cases.put_case(caseid, create_template(assays, percent, region, productPrices, Units, name, slateorblend, type, codes, seasonCode))
        return caseid
    except:
        cases.post_case(create_template(assays, percent, region, productPrices, Units, name, slateorblend, type, codes, seasonCode))
        x = cases.get_cases()
        caseid = int(x.query('Name == @name')['ID'].iloc[0])
        return caseid
