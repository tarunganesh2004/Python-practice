#lex_auth_01269442027919769669

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    total_chocolates = sum(chocolates_received)
    return total_chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return
    
    if child_id_rewarded not in child_id:
        print("Child id is invalid")
        return
    
    index = child_id.index(child_id_rewarded)
    chocolates_received[index] += extra_chocolates
    print(chocolates_received)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)