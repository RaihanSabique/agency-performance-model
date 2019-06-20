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

    def get_amount_analysis_result(self):
        new_df = self.data_df.filter(['year', 'nb_wrtn_prem_amt', 'total_wrtn_prem_amt','prev_wrtn_prem_amt','ernd_prem_amt','losses_amt'], axis=1)
        print(new_df)
        result_df=new_df.groupby(['year']).sum()
        print(result_df)
        data_dict = result_df.to_dict()
        print(data_dict)
        return data_dict