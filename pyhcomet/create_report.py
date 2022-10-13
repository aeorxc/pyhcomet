import pandas as pd
import create_case
import netback
import time

def create_report():
    caseID = create_case.create_and_post_case()
    nbID = netback.run_netback_case(caseID)
    while netback.get_run_status(nbID)[0] != 'complete':
        print(netback.get_run_status(nbID))
        time.sleep(5)
    report = netback.get_report(nbID)
    products = report.loc['Products'][0]
    products = pd.DataFrame(products)
    return products
