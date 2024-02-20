'''1) write a single program to handle the following arithmetic operations for addition, subtraction, 
multiplication , division, floor division,modulus and Exponentiation.'''


def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot find modulus with zero"
def exponentiation(a, b):
    return a ** b
def floor_division(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot perform floor division by zero"

print("The operations are: ")
print('1.Add')
print('2.sub')
print('3.mul')
print('4.div')
print('5.modulus')
print('6.exponentiation')
print('7.floor_div')
print('8.exit')

num1=float(input("enter a num1: "))
num2=float(input("enter a num2: "))
while 1:
    choice=input("enter u r choice: ")
    if choice=='8':
        print('enter a valid choice!! or exit')
        break  
    if choice=='1':
        print(addition(num1,num2))
    elif choice=='2':
        print(subtraction(num1,num2))
    elif choice=='3':
        print(multiplication(num1,num2))
    elif choice=='4':
        print(division(num1,num2))
    elif choice=='5':
        print(modulus(num1,num2))
    elif choice=='6':
        print(exponentiation(num1,num2))
    elif choice=='7':
        print(floor_division(num1,num2))
   
