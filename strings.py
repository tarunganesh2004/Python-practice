"""
f- string is used to format the string in python.
r-string is used to ignore the escape characters in the string.
"""

def demonstrate_f_and_r_strings():
    name = "Alice"
    age = 30

    # Using f-string
    f_string_example = f"My name is {name} and I am {age} years old."
    print(f_string_example)

    # Using r-string
    r_string_example = r"This is a raw string where \n is not treated as a newline."
    print(r_string_example)

demonstrate_f_and_r_strings()


# String methods

def demonstrate_string_methods():
    boarding_call = "Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."

    if(boarding_call.startswith("Good Evening")):
        print("The boarding call starts with 'Good Evening'")
    
    if(boarding_call.endswith("8.40A.M.")):
        print("The boarding call ends with '8.40A.M.'")

    if boarding_call.find("AL")>=0:
        print("The boarding call contains 'AL'")
    
    print("The index of 'final' in the boarding call is:", boarding_call.index("final"))
    print(boarding_call.upper())
    print(boarding_call.lower())
    print(boarding_call.replace("AL","Airline"))
    split_call = boarding_call.split(" ")
    print("The boarding call split into words is:", split_call)
    for i in split_call:
        if i.isdigit():
            print("it is digit")
        elif i.isalpha():
            print("it is alphabet")
        elif i.isalnum():
            print("it is alphanumeric")
        
    joined_call = "-".join(split_call)
    print("The boarding call joined with hyphens is:", joined_call)

    print(boarding_call.count("AL")) # used to count occurrences of a substring

    s="this is random test sentence"
    print(s.capitalize()) # capitalizes first letter of the string
    print(s.title()) # capitalizes first letter of each word in the string

    # now for substring
    s1="Hello, welcome"
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+1):
            print(s1[i:j]) # prints all substrings of s1
demonstrate_string_methods()


# task 
def task(p,src,dest):
    tickets=[]
    airline="AL1"

    src1=src[:3].upper()
    dest1=dest[:3].upper()

    ticketno=101

    for i in range(p):
        ticket=f"{airline}:{src1}::{dest1}:{ticketno}"
        tickets.append(ticket)
        ticketno+=1

    if len(tickets)<5:
        return tickets 
    else:
        return tickets[-5:]