# random module

import random 

def demonstrate_random_module():
    x=10
    y=50
    print(random.randint(x,y)) # generates random integer between x and y (both inclusive)
    print(random.random()) # generates random float between 0 and 1
    print(random.randrange(x,y)) # generates random integer between x and y (y exclusive)
    print(random.randrange(x,y,5)) # generates random integer between x and y with step 5
    print(random.uniform(x,y)) # generates random float between x and y

    l=["apple","banana","cherry","date"]
    print(random.choice(l)) # randomly selects an element from the list

    numbers=[1,2,3,4,5,6,7,8,9,10]
    print(random.choices(numbers,k=3)) # randomly selects k elements from the list with replacement
    print(random.sample(numbers, k=3)) # randomly selects k elements from the list without replacement

    random.shuffle(numbers) # shuffles the list in place
    print("Shuffled list:", numbers)


demonstrate_random_module()

# math module 
import math 

def demonstrate_math_module():
    num1=234.01
    num2=6
    num3=-27.01

    print(math.ceil(num1)) # returns the smallest integer greater than or equal to num1 --> 235
    print(math.floor(num1)) # returns the largest integer less than or equal to num1 --> 234
    print(math.sqrt(num2)) # returns the square root of num2 --> 2.449489742783178
    print(math.factorial(num2)) # returns the factorial of num2 --> 720
    print(math.fabs(num3)) # returns the absolute value of num3 --> 27.01
    print(math.pow(num2,3)) # returns num2 raised to the power of 3 --> 216.0
    print(math.gcd(48,18)) # returns the greatest common divisor of 48 and 18 --> 6
demonstrate_math_module()
