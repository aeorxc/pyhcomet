import cases
import create_slate
import create_price_set
import create_refinary_set


settings = {'SlateID': create_slate.create_and_post_slate(), 'RegionID': 'NWE',
            'SimplePriceSetID': None,
            'SimpleRefineryConfigID': create_refinary_set.create_and_post_ref_config(),
            'SimpleSeasonCode': 'INT', 'SimpleCutSetID': 0, 'SimpleSpecificationID': 1884, 'Name': 'TestAPI8'} #Post case doesnt seem to like SimplePriceSetID

casetemplate = {'Selected': False, 'Comment': '', 'SlateOrBlend': 0, 'SlateID': settings['SlateID'],
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

print(create_and_post_case())
