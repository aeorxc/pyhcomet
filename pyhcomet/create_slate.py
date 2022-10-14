import slates
import crudes

def get_assay_items(name: str):
    assays = crudes.get_crudes()
    crudecode = str(assays.query('Name == @name')['intCrudeID'].iloc[0])
    libary = str(assays.query('Name == @name')['Library'].iloc[0])
    gradeID = str(assays.query('Name == @name')['PTI_CIMSGradeID'].iloc[0])
    filepath = "D:~Haverly~HCOMET~AssayLibs~" + libary + "~" + crudecode + ".CRU"
    items = {'crudeCode': crudecode, 'library': libary, 'gradeID': gradeID, 'filepath': filepath, 'name': name}
    return items


def create_dict(items: dict):
    assay = {"LimitsAdv": [
        {"Selected": "true", "CrudeCode": items['crudeCode'], "Library": items['library'], "RunIndex": 1, "Min": "null",
         "Max": "null",
         "Fix": "null"}], "CustomPrices": [], "LimitsCustom": [], "WCProperties": [], "ID": "null", "Selected": "true",
        "Chart": "true", "Code": items['crudeCode'], "BlendID": "null", "Name": items['name'],
        "Library": items['library'],
        "Price": "null", "Freight": "null", "PTI_CIMSGradeID": items['gradeID'],
        "CRUFilePath": items['filepath'], "Year": "null", "Country": "null",
        "MinPer": "null", "MaxPer": "null", "FixPer": "null", "BatchPer": "null", "SortOrder": 1, "CustomCode": "null",
        "SPG": "null", "SPG_Calc": "null", "IsRowExpanded": "false", "Location": "null", "Period": "null",
        "Account": "null"}
    return assay


def create_list(names: list):
    assays = []
    for name in names:
        assay = create_dict(get_assay_items(name))
        assays.append(assay.copy())
    return assays

def create_template(assays: list, name: str):
    slatetemplate = {"SlateItems": assays, "LimitsAdvDetails": [{"Name": "null", "Selected": "true"}],
                     "LimitsCustomDetails": [], "IsAcctWide": "false", "MaxInBlend": "null", "OptimizeBlend": "false",
                     "SubstituteQty": "null",
                     "Chart": "false", "MinPer": "null", "SubQtyCustomFix": "null", "SubQtyCustomMin": "null",
                     "SubQtyCustomMax": "null",
                     "LimitsUnit": 0, "LimitsUnitCustom": 0, "SelectedSlateItemsCount": len(assays), "BlendOptRunCountAdv": 1,
                     "BlendOptRunCountCustom": "null", "BlendOptRunCountAdvSelected": 1,
                     "BlendOptRunCountCustomSelected": "null",
                     "Name": name}
    return slatetemplate


def create_and_post_slate(assays: list, name: str):
    x = slates.get_slates()
    listOfSlates = create_list(assays)
    template = create_template(listOfSlates, name)
    try:
        slateid = int(x.query('Name == @name')['ID'].iloc[0])
        slates.put_slate(slateid, template)
        return slateid
    except:
        slates.post_slate(template)
        x = slates.get_slates()
        slateid = int(x.query('Name == @name')['ID'].iloc[0])
        return slateid