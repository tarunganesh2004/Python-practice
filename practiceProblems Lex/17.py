 

train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]


def get_train_name (train_no):
    #start writing your code here
    for train in train_list:
        if train["train_no"]==train_no:
            return train["name"]
    
    return "Invalid Train_no"

def get_trains_for_day(day_of_run):
    #start writing your code here
    if day_of_run not in ['Mo','Tu','We','Th','Fr','Sa','Su']:
        return "Invalid Day"
    trains_running=[]
    for train in train_list:
        if day_of_run in train["days_of_run"]:
            trains_running.append(train["name"])
    return trains_running

def get_total_fare(train_no,passenger_dict):
    #start writing your code here
    for train in train_list:
        if train["train_no"]==train_no:
            total_fare=0
            total_fare+=passenger_dict.get("sleeper",0)*train["sleeper_fare"]
            total_fare+=passenger_dict.get("ac",0)*train["ac_fare"]
            return total_fare
    return "Invalid Train_no"
    
print(get_train_name(25627))
print(get_trains_for_day("Mo"))
print(get_total_fare(22642,{"sleeper":5, "ac":1}))

