#problem number-|--> 1
#Task 1: Calculate Factorial Using a Function.
def factorial(n):
   if n==1:
       return 1
   elif n<0:
       return "Negative numbers are  not allowed"
   elif n==0:
       return 1
   else:
       return n*factorial(n-1)
number = int(input("Enter a number: "))
print(f"factorial value of {number} is = {factorial(number)}")


