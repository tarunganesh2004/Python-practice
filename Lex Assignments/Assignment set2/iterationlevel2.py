def solve(heads, legs):
    error_msg = "No solution"
    if heads < 0 or legs < 0 or legs % 2 != 0:
        print(error_msg)
        return

    # c+r=heads
    # 2c+4r=legs
    rabbit_count = (legs - 2 * heads) // 2
    chicken_count = heads - rabbit_count

    if rabbit_count < 0 or chicken_count < 0:
        print(error_msg)
        return

    if 2 * chicken_count + 4 * rabbit_count != legs:
        print(error_msg)
        return

    print(chicken_count, rabbit_count)

    # Start writing your code here
    # Populate the variables: chicken_count and rabbit_count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(chicken_count,rabbit_count)
    # print(error_msg)


# Provide different values for heads and legs and test your program
solve(20,10)
