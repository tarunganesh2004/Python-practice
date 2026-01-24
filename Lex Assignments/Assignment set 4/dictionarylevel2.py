#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    crct=0 # correct words
    incrct=0 # wrong if more than 2 letters wrong
    almostcrct=0 # no more than 2 letters wrong

    for word in word_dict:
        cur_word=word_dict[word]
        if word==cur_word:
            crct+=1
        elif len(word)!=len(cur_word):
            incrct+=1
        else:
            # check difference
            diff=0
            length=min(len(word),len(cur_word))
            for i in range(length):
                if word[i]!=cur_word[i]:
                    diff+=1
            diff+=abs(len(word)-len(cur_word)) # if lengths are different
            if diff<=2:
                almostcrct+=1
            else:
                incrct+=1

    return [crct,almostcrct,incrct]


word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))