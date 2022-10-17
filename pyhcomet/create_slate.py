import slates
import crudes

def get_assay_items(name: str):
    assays = crudes.get_crudes()
    crudecode = str(assays.query('Name == @name')['intCrudeID'].iloc[0])
    libary = str(assays.query('Name == @name')['Library'].iloc[0])
    items = {'crudeCode': crudecode, 'library': libary}
    return items

def create_dict(items: dict):
    assay = {"Selected": "true", "Library": items['library'], "Code": items['crudeCode']}
    return assay

def create_list(names: list):
    assays = []
    for name in names:
        assay = create_dict(get_assay_items(name))
        assays.append(assay.copy())
    return assays

def create_template(assays: list, name: str):
    slatetemplate = {"SlateItems": assays, "Name": name}
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