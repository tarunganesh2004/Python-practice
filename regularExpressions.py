# to use regular expressions, we need to import re module
import re

# two commonly used methods in re module are search and sub
# search is used to find a pattern in a string
# sub is used to replace a pattern in a string with another string

s="The rain in Spain stays mainly in the plain"
re.search(r"ain",s)  # r indicates raw string
# returns a match object if pattern is found, else returns None


# if we want we can check a pattern in a random word 
if re.search(r"ain","rain"):
    print("Pattern found in the word 'rain'")
# to replace a pattern in a string with another string, we use sub
new_s=re.sub(r"ain","XXX",s) # replaces all occurrences of "ain" with "XXX"

print(new_s)

def demonstrate_regex_patterns():
    # .is used to match one occurrence of any character except newline
    pattern1 = r".at"
    test_string1 = "The cat sat on the mat."
    matches1 = re.findall(pattern1, test_string1)
    print("Matches for pattern '.at':", matches1)

    # ^.is used to match the start of a string
    pattern2 = r"^The"
    if(re.search(pattern2, test_string1)):
        print("The string starts with 'The'")

    # $.is used to match the end of a string