#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    #start writing your code here
    arr=sentence.split(" ")

    def rearrange(word):
        v="aeiouAEIOU"
        vl=[]
        cl=[]
        for ch in word:
            if ch.isalpha() and ch in v:
                vl.append(ch)
            else:
                cl.append(ch)
        return ''.join(cl+vl)
    for i in range(len(arr)):
        if i%2==0:
            arr[i]=arr[i][::-1]
        else:
            # rearrange 
            arr[i]=rearrange(arr[i])
    return ' '.join(arr)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)