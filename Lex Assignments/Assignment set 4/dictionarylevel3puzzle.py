# lex_auth_0127382283825971201450


def max_frequency_word_counter(data):
    # from collections import Counter
    res = ""
    frequency = 0
    arr=data.split(" ")
    # word_count=Counter(arr)
    def getCount(arr):
        count={}
        for word in arr:
            if word in count:
                count[word]+=1
            else:
                count[word]=1
        return count
    word_count=getCount(arr)
    print(word_count)
    max_freq=max(word_count.values())
    for word,freq in word_count.items():
        if freq==max_freq:
            if len(word)>len(res):
                res=word
                # frequency=freq
            frequency=freq
    print(res,frequency)

    # print(word,frequency)


# Provide different values for data and test your program.
data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
data1 = "Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
max_frequency_word_counter(data1)