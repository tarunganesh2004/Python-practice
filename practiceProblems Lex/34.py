
def check_well_formated(input_item,list_label):
    
    
    # input item is a list 
    if not isinstance(input_item,list):
        return False
    # length atleast 2
    if len(input_item) < 2:
        return False
    # input_item[0] is list_label
    if input_item[0]!=list_label:
        return False
    
    # each of the remaining items is either a string or well formatted list
    for item in input_item[1:]:
        if not (isinstance(item,str) or check_well_formated(item,list_label)):
            return False
    return True