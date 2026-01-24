#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    res=[]
    arr=data.split(" ")

    def encode(word):
        v="aeiouAEIOU"
        has_consonant=False 
        for ch in word:
            if ch not in v:
                has_consonant=True
                break
        if not has_consonant:
            return word
        
        res=""
        for ch in word:
            if ch not in v:
                res+=ch
        return res

    for w in arr:
        res.append(encode(w))
    return ' '.join(res)

def othersimpleMethod(data):
    words=data.split(" ")
    def encode(word):
        v="aeiouAEIOU"
        if all(ch in v for ch in word):
            return word
        return ''.join([ch for ch in word if ch not in v])
    
    return ' '.join([encode(word) for word in words])

data="I love Python"
print(sms_encoding(data))