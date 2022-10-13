import cases
import create_slate
import create_price_set
import refineries
import slates
import price_sets


settings = {'SlateID': slates.get_slate_id('Algeria'), 'RegionID': 'NWE',
            'SimplePriceSetID': price_sets.get_price_set_id('NWE', '1/1/2023'),
            'SimpleRefineryConfigID': refineries.get_ref_config('NWE', 'NWE Generic'),
            'SimpleSeasonCode': 'INT', 'SimpleCutSetID': 0, 'SimpleSpecificationID': 1884, 'Name': 'TestAPI8'}

casetemplate = {'Selected': True, 'Comment': '', 'SlateOrBlend': 0, 'SlateID': settings['SlateID'],
                'BlendID': None, 'CutSetID': None, 'ModelType': 0, 'RegionID': settings['RegionID'],
                'PriceSetType': 0, 'SimplePriceSetID': settings['SimplePriceSetID'], 'SimplePriceSetGroupID': None,
                'SimpleRefineryConfigID': settings['SimpleRefineryConfigID'],
                'SimpleSpecificationID': settings['SimpleSpecificationID'],
                'SimpleCutSetID': settings['SimpleCutSetID'], 'SimpleSeasonCode': settings['SimpleSeasonCode'],
                'AdvancedPriceSetID': None, 'AdvancedPriceSetGroupID': None, 'AdvancedRefineryConfigID': None,
                'AdvancedSpecificationID': None, 'AdvancedCutSetID': None, 'AdvancedSeasonCode': 'INT',
                'CustomModelID': None, 'CustomPriceSetID': None, 'CustomPriceSetGroupID': None,
                'CustomRefineryConfigID': None, 'CustomSpecificationID': None, 'CustomCutSetID': None,
                'CustomTransportID': None, 'CustomSeasonCode': None, 'Name': settings['Name']}


def create_and_post_case():
    cases.post_case(casetemplate)
    x = cases.get_cases()
    Name = settings['Name']
    caseid = x.query('Name == @Name')['ID'].iloc[0]
    return caseid
