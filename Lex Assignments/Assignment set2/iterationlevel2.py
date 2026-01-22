def solve(heads, legs):
    error_msg = "No solution"
    if legs%2!=0 or legs<2*heads or legs>4*heads:
        print(error_msg)
    chicken_count = 0
    rabbit_count = 0

    # c+r=heads
    # 2c+4r=legs

    rabbit_count=(legs - 2 * heads) // 2
    chicken_count=heads - rabbit_count

    if rabbit_count<0 or chicken_count<0:
        print(error_msg,end=" ")
    elif 2*chicken_count + 4*rabbit_count != legs and chicken_count + rabbit_count != heads:
        print(error_msg)
    else:
        print(chicken_count, rabbit_count)

    # Start writing your code here
    # Populate the variables: chicken_count and rabbit_count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(chicken_count,rabbit_count)
    # print(error_msg)


# Provide different values for heads and legs and test your program
solve(20,10)
