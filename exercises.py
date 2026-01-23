# generate next 15 leap years
def generate(year):
    ly=[]

    while len(ly)<15:
        if((year%4==0 and year%100!=0) or (year%400==0)):
            ly.append(year)
        year += 1
    return ly

print(generate(2023))


# string length encoding
def encode(s):
    res=""
    count=1

    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            res+=str(count)+s[i-1]
            count=1
    res+=str(count)+s[-1]
    return res

s="aaabbccccd"
print(encode(s))