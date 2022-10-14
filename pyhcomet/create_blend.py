import blends
import crudes

settings = {'Name': 'TestAPI'}
names = ["Agbami '07", "Agbami (GSC) July '18", "Agbami (CVX) Mar 16 '21"]
percent = {"Agbami '07": 33, "Agbami (GSC) July '18": 33, "Agbami (CVX) Mar 16 '21": 34}

def get_assay_items(name: str):
    assays = crudes.get_crudes()
    crudecode = str(assays.query('Name == @name')['intCrudeID'].iloc[0])
    libary = str(assays.query('Name == @name')['Library'].iloc[0])
    gradeID = str(assays.query('Name == @name')['PTI_CIMSGradeID'].iloc[0])
    filepath = "D:~Haverly~HCOMET~AssayLibs~" + libary + "~" + crudecode + ".CRU"
    items = {'crudeCode': crudecode, 'library': libary, 'gradeID': gradeID, 'filepath': filepath, 'name': name}
    return items

def create_dict(items: dict, percent: dict):
    assay = {"CustomPrices": [], "FixedCutFilterValues": ["null", "null", "null", "null", "null", "null"],
     "FixedCutFilterValuesCalc": ["false", "false", "false", "false", "false", "false"],
     "DynamicCutFilterValues": ["null", "null", "null", "null", "null", "null"], "WCProperties": [], "Percent": percent[items['name']],
     "FixPer": "Float", "Selected": "false", "SelectedToAdd": "false", "ID": "null", "Region": "null",
     "Price": "null", "Freight": "null", "CRUFilePath": items['filepath'],
     "CrudeType": "null", "SulfurType": "null", "State": "null", "Date": "null", "Quality": "null", "PTICrdId": "null",
     "intCrudeID": "null", "Title1": "null", "Title2": "null", "Owner": "null", "ShareOwned": "null",
     "SampleID": "null", "Reference": "null", "Production": "null", "SmoothDataConf": "null", "Laboratory": "null",
     "LabSourceRef": "null", "LoadPort": "null", "LPCode": "null", "UserDefRegion": "null", "PTI_CIMSUrl": "null",
     "Comments": "null", "CutValue": "null", "IsCutValueCalc": "false", "BlendID": "null", "Sites": "null",
     "CustomCode": "null", "PropVal01": "null", "PropVal02": "null", "PropVal03": "null", "PropVal04": "null",
     "PropVal05": "null", "PropVal06": "null", "PropVal07": "null", "PropVal08": "null", "Code": items['crudeCode'],
     "Name": items['name'], "Library": items['library'], "Year": "null", "Country": "null",
     "PTI_CIMSGradeID": items['gradeID'], "ChemicalClass": "null", "CRUFileSource": "null", "N2": "null", "TAN": "null",
     "POUR": "null", "API": "null", "API_Calc": "null", "SUL": "null"}
    return assay

def create_list(names: list, percent: dict):
    assays = []
    for name in names:
        assay = create_dict(get_assay_items(name), percent)
        assays.append(assay.copy())
    return assays

def create_template(assays: list, name: str):
    blendtemplate = {"BlendComponentCrudes": assays, "WCProperties": [], "WCPropertiesCustom": [], "Selected": "false",
            "IsAcctWide": "false", "PctType": 0, "Name": name}
    return blendtemplate


def create_and_post_blend(assays: list, percent: dict, name: str):
    x = blends.get_blends()
    listOfBlends = create_list(assays, percent)
    template = create_template(listOfBlends, name)
    try:
        blendid = int(x.query('Name == @name')['ID'].iloc[0])
        blends.put_blend(blendid, template)
        return blendid
    except:
        blends.post_blend(template)
        x = blends.get_blends()
        blendid = int(x.query('Name == @name')['ID'].iloc[0])
        return blendid
