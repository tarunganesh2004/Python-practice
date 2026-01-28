# close number

def close_number(num1,num2,num3):
    def close(a,b):
        return abs(a-b)<=1
    def far(a,b):
        return abs(a-b)>=2
    
    if close(num1,num2) and far(num1,num3) and far(num2,num3):
        return True
    if close(num1,num3) and far(num1,num2) and far(num2,num3):
        return True
    if close(num2,num3) and far(num1,num2) and far(num1
,num3):
        return True
    return False

print(close_number(1,2,10))