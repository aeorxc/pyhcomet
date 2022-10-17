import price_sets


def get_items(name: str, productPrices: dict, Units: dict, i: int, codes: dict):
    template = {"Code": codes[name], "Description": name,
                "Selected": "true", "Price": productPrices[name], "PriceUnit": Units[name], "RateUnit": "Vol%",
                "Number": i,
                "Type": 0, "LPCode": name}
    return template


def create_list_of_prices(productPrices: dict, Units: dict, codes: dict):
    listofproducts = []
    i = 1
    for name, value in productPrices.items():
        template = get_items(name, productPrices, Units, i, codes)
        listofproducts.append(template.copy())
        i = i + 1
    return listofproducts


def get_price_template(listofproducts: list, name: str):
    price_set_template = {"Products": listofproducts, "Selected": "true", "Name": name}
    return price_set_template


def create_and_post_price_set(productPrices: dict, Units: dict, name: str, region: str, codes: dict):
    x = price_sets.get_price_sets(region)
    listofprices = create_list_of_prices(productPrices, Units, codes)
    template = get_price_template(listofprices, name)
    try:
        priceid = int(x.query('Name == @name')['ID'].iloc[0])
        price_sets.put_price_set(region, priceid, template)
        return priceid
    except:
        price_sets.post_price_set(template, region)
        x = price_sets.get_price_sets(region)
        priceid = int(x.query('Name == @name')['ID'].iloc[0])
        return priceid
