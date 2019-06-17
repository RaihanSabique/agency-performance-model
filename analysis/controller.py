import pandas as pd
import analysis.byagency as byAgency
class manage:

    def __init__(self,data_df,product_list,state_list):
        self.data_df=data_df
        self.product_list=product_list
        self.state_list=state_list


    def get_state_analysis_result(self):
        #print(self.data_df)
        dict_result=byAgency.state_count(self.data_df,self.state_list)
        return dict_result

    def get_product_line_result(self):
        dict_result=byAgency.product_line(self.data_df)
        return dict_result

    def get_pl_cl_product(self):
        dict_result=byAgency.product_type(self.data_df,self.product_list)
        return dict_result