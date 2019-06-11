import pandas as pd
import json

def state_count(df,state_list):
    print(df.state_abbr_id)
    print(state_list)
    #df = df.groupby('state_abbr_id')['state_abbr_id'].nunique()
    df_result=pd.DataFrame()
    df_result=df.state_abbr_id.value_counts()
    print(df_result)
    data_dict = df_result.to_dict()
    print(data_dict)
    result={}
    data_dict_state={}
    for state in state_list:
        if state['ID'] in data_dict.keys():
            data_dict_state[state['STATE_ABBR']]=data_dict[state['ID']]
        else:
            data_dict_state[state['STATE_ABBR']] = 0

    print(data_dict_state)
    return data_dict_state