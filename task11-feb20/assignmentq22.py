'''22) Write a Python program to check if a given number is a perfect number.'''


n=int(input("enter a num: "))
def is_perfect(number):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==number
if is_perfect(n):
    print('num is perfect')
else:
    print('not perfect')