# task
def check(l):

    c=0
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            c+=1
    return c

l=[1,1,5,100,-20,-20,6,0,0]
print(check(l))