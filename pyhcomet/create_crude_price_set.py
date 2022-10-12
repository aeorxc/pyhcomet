import crude_price_sets

settings = {'Name': 'TestAPI3', 'Region':'NWE', 'Crudes' : ['AABKH2001']}

crude_price_template = {"Crudes": settings['Crudes'],"IsAcctWide":"false","IsDelete":"false","Name": settings['Name']}

def create_and_post_crude_price_set():
    crude_price_sets.post_crude_price_set(crude_price_template, settings['Region'])
    x = crude_price_sets.get_crude_price_sets('NWE')
    Name = settings['Name']
    crudepriceid = int(x.query('Name == @Name')['ID'].iloc[0])
    return crudepriceid