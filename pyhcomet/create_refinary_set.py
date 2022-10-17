import refineries

settings = {'Name': 'Test', 'Region': 'NWE'}

refinarytemplate = {
    "Refineries": [{"Units": [{ "Code": "ADU", "Name": "Atm. Dist. Unit",
                                "Enabled": "true",
                               "Capacity": 100000.0, "Rate": "null", "MinRate": "null"},
                              {
                               "Code": "ISO", "Name": "Isomerization", "Enabled": "true",  "Capacity": "null", "Rate": "null",
                               "MinRate": "null",
                               },
                              { "Code": "ALK", "Name": "Alkylation", "Enabled": "false",
                               "Capacity": "null",
                               "Rate": "null", "MinRate": "null"},
                              { "Code": "REF", "Name": "Reformer",
                               "Enabled": "true",
                               "Capacity": 20000.0, "Rate": "null", "MinRate": "null"},
                              {
                               "Code": "DSNLVN", "Name": "ADU Naph Desulf", "Enabled": "true", "Capacity": 20000.0,
                               "Rate": "null", "MinRate": "null"},
                              {"Code": "DSKKER", "Name": "ADU Kero Desulf",
                               "Enabled": "true", "Capacity": 15000.0, "Rate": "null", "MinRate": "null",
                              },
                              { "Code": "DSGLGO", "Name": "ADU LGO Desulf",

                               "Enabled": "true", "Capacity": 25000.0, "Rate": "null", "MinRate": "null",
                              },
                              {"Code": "DSGHGO", "Name": "ADU HGO Desulf",
                               "Enabled": "true", "Capacity": 25000.0, "Rate": "null", "MinRate": "null",
                               },
                              { "Code": "ARC", "Name": "Atm Resid Cracker",
                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                               },
                              {"Code": "VDU", "Name": "Vac. Dist. Unit",
                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                              },
                              { "Code": "DSGLVG", "Name": "VDU LGO Desulf",
                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                               },
                              {"Code": "DSGHVG", "Name": "VDU HGO Desulf",
                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                              },
                              {"Code": "FCC", "Name": "Cat Cracker",
                               "Enabled": "false",
                               "Capacity": "null", "Rate": "null", "MinRate": "null"},
                              {"Code": "DSNCCN", "Name": "ARC / FCC NAPH Desulf",
                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                               },
                              {"Code": "DSGCLC", "Name": "ARC / FCC LCO Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                               },
                              {"Code": "DSGCHC", "Name": "ARC / FCC HCO Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                              },
                              { "Code": "HCR", "Name": "Hydrocracker",
                               "Enabled": "false",
                               "Capacity": "null", "Rate": "null", "MinRate": "null", },
                              { "Code": "VBR", "Name": "Visbreaker",
                              "Enabled": "false",
                               "Capacity": "null", "Rate": "null", "MinRate": "null", },
                              { "Code": "DSNVNA", "Name": "Visbreaker Naph Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                              },
                              { "Code": "DSGVGO", "Name": "Visbreaker GO Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                               },
                              {"Code": "COK", "Name": "Coker", "UnitIndex": 21,
                               "Enabled": "false",
                               "Capacity": "null", "Rate": "null", "MinRate": "null", },
                              { "Code": "DSNKNA", "Name": "COK Naph Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                               },
                              {"Code": "DSGKLG", "Name": "COK LGO Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                              },
                              {"Code": "DSGKHG", "Name": "COK HGO Desulf",

                               "Enabled": "false", "Capacity": "null", "Rate": "null", "MinRate": "null",
                             },
                              {"Code": "DAS", "Name": "Deasphaltor",  "Enabled": "false",
                               "Capacity": "null", "Rate": "null", "MinRate": "null", },
                              {"Code": "ASP", "Name": "Asphalt Mfg", "Enabled": "false",
                               "Capacity": "null", "Rate": "null", "MinRate": "null", }], "ID": 1,
                     "Name": "Test", "Selected": "true",
                    "IsSelected": "true", "SelectedRefineriesCount": 1,
    "Name": settings['Name']}]}

def create_and_post_ref_config():
    x = refineries.get_refinary_configs(settings['Region'])
    Name = settings['Name']
    try:
        configid = int(x.query('Name == @Name')['ID'].iloc[0])
        refineries.put_refinary_config(refinarytemplate, settings['Region'], configid)
        return configid
    except:
        refineries.post_refinary_config(refinarytemplate, settings['Region'])
        x = refineries.get_refinary_configs(settings['Region'])
        configid = int(x.query('Name == @Name')['ID'].iloc[0])
        return configid
