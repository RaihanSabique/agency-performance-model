import pandas as pd
import json
from importdata import converter

def state_count(df,state_list):
    #print(df.state_abbr_id)
    #print(state_list)
    #df = df.groupby('state_abbr_id')['state_abbr_id'].nunique()
    df_result=pd.DataFrame()
    df_result=df.state_abbr_id.value_counts()
    #print(df_result)
    data_dict = df_result.to_dict()
    #print(data_dict)
    result={}
    data_dict_state={}
    for state in state_list:
        if state['ID'] in data_dict.keys():
            data_dict_state[state['STATE_ABBR']]=data_dict[state['ID']]
        else:
            data_dict_state[state['STATE_ABBR']] = 0

    print(data_dict_state)
    del df_result
    return data_dict_state

def product_line(df):
    print(df.prod_line)
    data_dict={}
    df_result = df.prod_line.value_counts()
    data_dict = df_result.to_dict()
    if('CL' not in data_dict):
        data_dict['CL'] = 0
    if('PL' not in data_dict):
        data_dict['PL'] = 0
    print(data_dict)
    total=data_dict['CL']+data_dict['PL']
    print(total)
    data_dict['CL']=round((float)(data_dict['CL']/total)*100,2)
    data_dict['PL'] = round((float)(data_dict['PL'] / total) * 100,2)
    print(data_dict)
    del df_result
    return data_dict

def product_type(df,product_list):
    grouped=df.groupby(['prod_abbr_id', 'prod_line']).groups
    #print(product_list)
    dict_result={}
    cl=[]
    pl=[]
    for name, group in grouped:
        print(name)
        print(group)
        if(group=="CL"):
            cl.append(converter.get_product_name(name,product_list))
        if(group=='PL'):
            pl.append(converter.get_product_name(name,product_list))
    print(cl,pl)
    dict_result['CL']=cl
    dict_result['PL']=pl
    return dict_result



