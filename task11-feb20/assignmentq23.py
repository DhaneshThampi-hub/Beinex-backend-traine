'''23) Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.(gcd(48, 
60)=12)'''



def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("enter a num1:"))
num2 = int(input("enter a num2:"))
gcd_result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")
