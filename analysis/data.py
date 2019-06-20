import pandas as pd

class data:
    data_df=pd.DataFrame
    product_list=[]
    state_list=[]

    def __init__(self):
        print("created")

    def setData(self,df,p_list,s_list):
        self.data_df=df
        self.product_list=p_list
        self.state_list=s_list

    def getDataDf(self):
        return self.data_df

    def getProductList(self):
        return self.product_list
    def getStateList(self):
        return self.state_list