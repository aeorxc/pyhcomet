import price_sets

settings = {'Name': 'TestAPI3'}

price_set_template = {"Crudes":[],"IsAcctWide":"false","IsDelete":"false","Name": settings['Name']}

def create_and_post_price_set():
    price_sets.post_crude_price(price_set_template, 'NWE')
    x = price_sets.get_price_sets('NWE')
    Name = settings['Name']
    priceid = int(x.query('Name == @Name')['ID'].iloc[0])
    return priceid