import cases
import create_slate
import create_price_set
import refineries
import create_blend

def create_template(assays: list, percent: dict, region: str, productPrices: dict, blendPurchasesPrices: dict, processPurchasesPrices: dict, Units: dict, name: str, slateorblend: int, type: str):
    settings = {'SlateID': create_slate.create_and_post_slate(assays, name), 'BlendID': create_blend.create_and_post_blend(assays, percent, name), 'RegionID': region,
                'SimplePriceSetID': create_price_set.create_and_post_price_set(productPrices, blendPurchasesPrices, processPurchasesPrices,
                                  Units, name, region),
                'SimpleRefineryConfigID': refineries.get_ref_config(region, type),
                'SimpleSeasonCode': 'INT', 'SimpleCutSetID': 0, 'SimpleSpecificationID': 1884, 'Name': 'TestAPI'}

    casetemplate = {'Selected': True, 'Comment': '', 'SlateOrBlend': slateorblend, 'SlateID': settings['SlateID'],
                    'BlendID': settings['BlendID'], 'CutSetID': None, 'ModelType': 0, 'RegionID': settings['RegionID'],
                    'PriceSetType': 0, 'SimplePriceSetID': settings['SimplePriceSetID'], 'SimplePriceSetGroupID': None,
                    'SimpleRefineryConfigID': settings['SimpleRefineryConfigID'],
                    'SimpleSpecificationID': settings['SimpleSpecificationID'],
                    'SimpleCutSetID': settings['SimpleCutSetID'], 'SimpleSeasonCode': settings['SimpleSeasonCode'],
                    'AdvancedPriceSetID': None, 'AdvancedPriceSetGroupID': None, 'AdvancedRefineryConfigID': None,
                    'AdvancedSpecificationID': None, 'AdvancedCutSetID': None, 'AdvancedSeasonCode': 'INT',
                    'CustomModelID': None, 'CustomPriceSetID': None, 'CustomPriceSetGroupID': None,
                    'CustomRefineryConfigID': None, 'CustomSpecificationID': None, 'CustomCutSetID': None,
                    'CustomTransportID': None, 'CustomSeasonCode': None, 'Name': name}
    return casetemplate

def create_and_post_case(assays: list, percent: dict, region: str, productPrices: dict, blendPurchasesPrices: dict, processPurchasesPrices: dict, Units: dict, name: str, slateorblend: int, type: str):
    x = cases.get_cases()
    try:
        caseid = int(x.query('Name == @name')['ID'].iloc[0])
        cases.put_case(caseid, create_template(assays, percent, region, productPrices, blendPurchasesPrices, processPurchasesPrices, Units, name, slateorblend, type))
        return caseid
    except:
        cases.post_case(create_template(assays, percent, region, productPrices, blendPurchasesPrices, processPurchasesPrices, Units, name, slateorblend, type))
        x = cases.get_cases()
        caseid = int(x.query('Name == @name')['ID'].iloc[0])
        return caseid
