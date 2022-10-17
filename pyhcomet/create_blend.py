import blends
import crudes

def get_assay_items(name: str):
    assays = crudes.get_crudes()
    crudecode = str(assays.query('Name == @name')['intCrudeID'].iloc[0])
    libary = str(assays.query('Name == @name')['Library'].iloc[0])
    items = {'crudeCode': crudecode, 'library': libary, 'name': name}
    return items

def create_dict(items: dict, percent: dict):
    assay = {"Percent": percent[items['name']], "Code": items['crudeCode'], "Library": items['library'], "Selected": "true"}
    return assay

def create_list(names: list, percent: dict):
    assays = []
    for name in names:
        assay = create_dict(get_assay_items(name), percent)
        assays.append(assay.copy())
    return assays

def create_template(assays: list, name: str):
    blendtemplate = {"BlendComponentCrudes": assays, "Name": name}
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
