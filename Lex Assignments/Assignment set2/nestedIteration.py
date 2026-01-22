# lex_auth_012693813706604544157


def find_max(num1, num2):
    max_num = -1
    if num1 >= num2:
        return -1

    def check(num):
        if len(str(num)) != 2:
            return False

        s = 0
        for digit in str(num):
            s += int(digit)
        return s % 3 == 0

    for i in range(num1, num2 + 1):
        if check(i) and i % 5 == 0:
            max_num = max(max_num, i)
    return max_num


# Provide different values for num1 and num2 and test your program.
max_num = find_max(10, 15)
print(max_num)
