import pandas as pd
import create_case
import netback
import time
from qe import qe


def create_report(assays: list, percent: dict, region: str, productPrices: dict, blendPurchasesPrices: dict,
                  processPurchasesPrices: dict, Units: dict, name: str, slateorblend: int, type: str):
    caseID = create_case.create_and_post_case(assays, percent, region, productPrices, blendPurchasesPrices,
                                              processPurchasesPrices, Units, name, slateorblend, type)
    nbID = netback.run_netback_case(caseID)
    while netback.get_run_status(nbID)[0] != 'complete':
        print(netback.get_run_status(nbID))
        time.sleep(5)
    report = netback.get_report(nbID)
    x = len(report.columns)
    res = pd.DataFrame()
    while x !=0:
        products = report.loc['Products'][x-1]
        products = pd.DataFrame(products)
        res = pd.concat([res, products], axis=1)
        x = x-1
    return res


productPrices = {'LPG': 650, 'Naphtha': 700, 'Mogas Prem 95': 830, 'Mogas Reg 92': 820, 'Jet-A1': 1060,
                 'Diesel 10ppm S': 1010, 'Diesel 50ppm S': 'null', 'Heating Oil 0.1% S': 980,
                 'Heating Oil 0.2% S': 'null',
                 'Fuel Oil 0.5% S': 600, 'Fuel Oil 1% S': 530, 'Fuel Oil 3.5% S': 470, 'Bitumen': 'null',
                 'Coke (HQ)': 'null',
                 'Coke (LQ)': 'null', 'Vac Gasoil': 'null', 'Atm Resid': 'null'}

blendPurchasesPrices = {'Feedstock LPG': 'null', 'Feedstock Lt Naphtha': 'null', 'Feedstock Alkylate': 'null'}

processPurchasesPrices = {'Feedstock Hv Naphtha': 'null', 'Feedstock VGO': 'null', 'Coker feed': 'null',
                          'Natural Gas for Fuel': 'null'}

Units = {'LPG': '$/MT', 'Naphtha': '$/MT', 'Mogas Prem 95': '$/MT', 'Mogas Reg 92': '$/MT', 'Jet-A1': '$/MT',
         'Diesel 10ppm S': '$/MT', 'Diesel 50ppm S': '$/bbl', 'Heating Oil 0.1% S': '$/MT',
         'Heating Oil 0.2% S': '$/bbl',
         'Fuel Oil 0.5% S': '$/MT', 'Fuel Oil 1% S': '$/MT', 'Fuel Oil 3.5% S': '$/MT', 'Bitumen': '$/MT',
         'Coke (HQ)': '$/MT',
         'Coke (LQ)': '$/MT', 'Vac Gasoil': '$/MT', 'Atm Resid': '$/bbl', 'Feedstock LPG': '$/bbl',
         'Feedstock Lt Naphtha': '$/bbl', 'Feedstock Alkylate': '$/bbl', 'Feedstock Hv Naphtha': '$/bbl',
         'Feedstock VGO': '$/bbl', 'Coker feed': '$/bbl',
         'Natural Gas for Fuel': '$/Mbtu'}

percent = {"Agbami '07": 33, "Agbami (GSC) July '18": 33, "Agbami (CVX) Mar 16 '21": 34}

assays = ["Agbami '07", "Agbami (GSC) July '18", "Agbami (CVX) Mar 16 '21"]

region = 'NWE'

type = 'NWE Generic'

name = 'debug1'

slateorblend = 0

qe.qe(create_report(assays, percent, region, productPrices, blendPurchasesPrices, processPurchasesPrices, Units, name,
                    slateorblend, type))
