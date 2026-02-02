def numberToEnglish(n):
    if n==0:
        return "zero"
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    res=""

    # if n==1000:
    #     return "one thousand"
    # if n>1000:
    #     res+=ones[n//1000]+" thousand"
    #     n=n%1000
    #     if n>0:
    #         res+=" " generally no need 
    if n>=100:
        res+=ones[n//100]+" hundred"
        n=n%100
        if n>0:
            res+=" and "
    if n>=20:
        res+=tens[n//10]
        n=n%10
        if n>0:
            res+=" "
    elif n>=10:
        res+=teens[n-10]
        n=0
    if n>0:
        res+=ones[n]

    return res

# print n fibonacci numbers
def fibonacci(n):
    res=[]
    a,b=0,1
    for _ in range(n):
        res.append(a)
        a,b=b,a+b
    return res

# leap year
def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
#prime or not 
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# strong number
def isStrongNumber(n):
    def fact(n):
        if n==0 or n==1:
            return 1
        return n*fact(n-1)
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=fact(digit)
        temp//=10
    return sum==n

# amicable numbers
def areAmicable(num1,num2):
    #proper divisors sum 
    s1=0
    s2=0
    for i in range(1,num1):
        if num1%i==0:
            s1+=i
    for i in range(1,num2):
        if num2%i==0:
            s2+=i
    return s1==num2 and s2==num1

# find common characters
def find_common(str1,str2):
    if not str1 or not str2:
        return ""
    
    return "".join(sorted(set(str1).intersection(set(str2))))
msg1="I like Python"
msg2="Java is a very popular language"
print(find_common(msg1,msg2))
