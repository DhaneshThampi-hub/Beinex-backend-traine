# Using for loop 
n=int(input("Enter the number of terms: "))
a=0 
b=1 
if n<=0:
    print("The Output of your input is",a)
else:
    print(a,b,end=" ")
    for x in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c


# Using while loop 
n = int(input("Enter the value of nth term: ")) 
a = 0 
b = 1 
c = 0 
count = 1 
print("Fibonacci Series: ", end = " ") 
while(count <= n):
    print(c, end = " ") 
    count += 1 
    a = b 
    b = sum 
    sum = a + b