def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # Start writing your code here
    # Populate the variables: five_needed and one_needed

    if no_of_five * 5 + no_of_one < rupees_to_make:
        print(-1)
        return
    five_needed=min(rupees_to_make//5,no_of_five)
    remaining=rupees_to_make-five_needed*5

    if remaining<=no_of_one:
        one_needed=remaining
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)
    # print("No. of Five needed :", five_needed)
    # print("No. of One needed  :", one_needed)
    # print(-1)


# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28, 8, 5)
