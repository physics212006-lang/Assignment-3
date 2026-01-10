# Task 2: Using the Math Module for Calculations
import math
#Take input from user
number = float(input("Enter a number: "))
#Using math module calculate the operations on the number
if  number < 0:
    print(f"Sorry, {number} is not a positive number,so only sine of the number i calculated")
    sine=math.sin(number)
    print(f"sine of {number} is {sine}")

elif number>0:
     print(f"The square root of {number} = {math.sqrt(number)}")
     print(f"The natural log  of {number}= {math.log(number)}")
     print(f"The sine of {number}= {math.sin(number)}")
elif number==0:
    print(f"The sine  of {number} is ={math.sin(number)}")
    print(f"The natural log  of {number}= {math.sqrt(number)}")



