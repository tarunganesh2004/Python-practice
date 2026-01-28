def integer_to_english(number):
    if number > 1000 or number < 0:
        return -1

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    if number == 0:
        return "zero"

    if number == 1000:
        return "one thousand"

    result = ""

    # Hundreds
    if number >= 100:
        result += ones[number // 100] + " hundred"
        number = number % 100
        if number > 0:
            result += " and "

    # Tens
    if number >= 20:
        result += tens[number // 10]
        number = number % 10
        if number > 0:
            result += " "

    # Teens
    elif number >= 10:
        result += teens[number - 10]
        number = 0

    # Ones
    if number > 0:
        result += ones[number]

    return result.strip()


print(integer_to_english(789))
