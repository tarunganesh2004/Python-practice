# lex_auth_012693825794351104168


def find_common_characters(msg1, msg2):
    res=""
    for ch in msg1:
        if ch in msg2 and ch not in res:
            res+=ch
    return res if res else -1


# Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
