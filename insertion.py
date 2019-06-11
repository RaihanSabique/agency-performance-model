import pandas as pd
import numpy as np
import pprint

import model as model


class insert:
    def __init__(self):
        print('init')
    def getData(self):
        df = pd.read_csv("../srccode/dataset/finalapi.csv")
        # df.read_csv("/srccode/dataset/finalapi.csv")
        prod_list=df.PROD_ABBR.unique()
        state_list=df.STATE_ABBR.unique()

        id=1
        for prod in prod_list:
            new_prod = model.Product_abbreviation(ID=id,
                             PROD_ABBR=prod)
    
            db.session.add(new_prod)
            db.session.commit()
            id+=1

        #model.Product_abbreviation.query.delete()
        prods = model.Product_abbreviation.query.all()
        output = []
        for p in prods:
            p_data = {}
            p_data['ID'] = p.ID
            p_data['PROD_ABBR'] = p.PROD_ABBR
            output.append(p_data)
        print(output)

