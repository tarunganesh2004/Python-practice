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


# longest consecutive sequence
def longest_consecutive(a):
    s = set(a)
    ans = 0
    for x in s:
        if x - 1 not in s:
            cur = x
            length = 1
            while cur + 1 in s:
                cur += 1
                length += 1
            ans = max(ans, length)
    return ans

def longest_palindrome(s):
    def ispal(s):
        return s==s[::-1]
    maxlen=0
    res=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            substr=s[i:j+1]
            if ispal(substr) and len(substr)>maxlen:
                maxlen=len(substr)
                res=substr
    return res

#compare dict frequency
def sort_dict(sentence):
    from collections import Counter
    words=sentence.split()
    freq=Counter(words)
    max_freq=0
    res=""
    for word,count in freq.items():
        # if same frequency choose longer word
        if count>max_freq or (count==max_freq and len(word)>len(res)):
            max_freq=count
            res=word

# pascal triangle
def pascal_triangle(n):
    triangle=[]
    for i in range(n):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return triangle

# PATTERNS  
def demonstrate_patterns():
    # Pattern 1: Right-angled triangle
    n = 5
    print("Right-angled triangle:")
    for i in range(1, n + 1):
        print("* " * i)

    # Pattern 2: Inverted right-angled triangle
    print("\nInverted right-angled triangle:")
    for i in range(n, 0, -1):
        print("* " * i)

    # Pattern 3: Pyramid
    print("\nPyramid:")
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    
    # inverted pyramid
    print("\nInverted Pyramid:")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

    # Pattern 4: Diamond
    print("\nDiamond:")
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "* " * (i + 1))

def max_subarray_sum(a):
    cur = best = a[0]
    for i in range(1, len(a)):
        cur = max(a[i], cur + a[i])
        best = max(best, cur)
    return best

def is_armstrong(n):
    p = len(str(n))
    return n == sum(int(d) ** p for d in str(n))

def trailing_zeros(n):
    cnt = 0
    while n:
        n //= 5
        cnt += n
    return cnt
