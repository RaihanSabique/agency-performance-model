
def get_prod_id(prod_name,prod_list):
    for prod in prod_list:
        if(prod["PROD_ABBR"]==prod_name):
            return prod["ID"]

def get_state_id(state_name,state_list):
    for state in state_list:
        if(state["STATE_ABBR"]==state_name):
            return state["ID"]

def get_product_name(prod_id,prod_list):
    for prod in prod_list:
        if(prod["ID"]==prod_id):
            return prod["PROD_ABBR"]