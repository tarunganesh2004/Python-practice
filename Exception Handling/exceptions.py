"""
Docstring for Exception Handling.exceptions
Common Built-in Exceptions

Exception	When it occurs
ZeroDivisionError	divide by zero
ValueError	wrong value type
TypeError	wrong data type
FileNotFoundError	missing file
IndexError	invalid index
KeyError	missing dictionary key
"""

# try:
#     print(10/0)
# except:
#     print("ZeroDivisionError: division by zero")

try:
    x=int("abc")
except ValueError:
    print("ValueError: invalid literal for int() with base 10: 'abc'")


# Multiple Exceptions
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")
except ValueError:
    print("ValueError: invalid literal for int() with base 10")