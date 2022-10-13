import slates

settings = {'Name': 'Algeria2'}

slatetemplate = {'SlateItems': [{'LimitsAdv': [{'Selected': True, 'CrudeCode': 'SAHB2013',
                'Library': 'COMET', 'RunIndex': 1, 'Min': None, 'Max': None, 'Fix': None}],
                'CustomPrices': [], 'LimitsCustom': [], 'WCProperties': [], 'ID': None, 'Selected': True,
                'Chart': True, 'Code': 'SAHB2013', 'BlendID': None, 'Name': "Saharan Blend '13", 'Library': 'COMET',
                'Price': None, 'Freight': None, 'PTI_CIMSGradeID': 'SAHARANBLD',
                'CRUFilePath': 'D:~Haverly~HCOMET~AssayLibs~COMET~SAHB2013.CRU', 'Year': None, 'Country': None,
                'MinPer': None, 'MaxPer': None, 'FixPer': None, 'BatchPer': None, 'SortOrder': 1,
                'CustomCode': None, 'SPG': None, 'SPG_Calc': None, 'IsRowExpanded': False, 'Location': None,
                'Period': None, 'Account': None}], 'LimitsAdvDetails': [{'Name': None, 'Selected': True}],
                'LimitsCustomDetails': [], 'IsAcctWide': False, 'MaxInBlend': None, 'OptimizeBlend': False,
                'SubstituteQty': None, 'Chart': False, 'MinPer': None, 'SubQtyCustomFix': None, 'SubQtyCustomMin': None,
                'SubQtyCustomMax': None, 'LimitsUnit': 0, 'LimitsUnitCustom': 0, 'SelectedSlateItemsCount': 1,
                'BlendOptRunCountAdv': 1, 'BlendOptRunCountCustom': None, 'BlendOptRunCountAdvSelected': 1,
                'BlendOptRunCountCustomSelected': None, 'Name': 'Algeria2'}


def create_and_post_slate():
    slates.post_slate(slatetemplate)
    x = slates.get_slates()
    Name = settings['Name']
    slateid = int(x.query('Name == @Name')['ID'].iloc[0])
    return slateid
