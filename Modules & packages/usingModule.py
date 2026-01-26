from test_function import test, PI

import test_function as tf

result = test(5, 10)
print(f"Result of test function: {result}")
print(f"Value of PI from test_function module: {PI}")

# __name__ and __main__ demonstration
# this is used to check if the module is being run directly or imported
# it helps in controlling the execution of code