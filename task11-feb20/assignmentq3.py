'''3) print the following patterns:
a)
0
0 0
0 0 0
0 0 0 0
'''
n=int(input('enter number of rows:  '))
for i  in range(n):
    for j in range(i+1):
        print('0',end=" ")
    print()
'''b)
      *
    * * *
  * * * * *
 * * * * * * *
'''
l=int(input("enter a row: "))
for i in range(l):
    k=2*(n-i)
    for k in range(k):
        print(end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

'''c)
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5'''

b=int(input("enter rows: "))
for i in range(b):
    for j in range(i+1):
        print(i,end=" ")
    print()

'''d)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''

s=int(input('enter number of rows: '))
for i in range(s+1):
    n=1
    for j in range(1,i+1):
        print(n,end=' ')
        n=n+1
    print()
'''e)
* * * * * *
* * * * *
* * * *
* * * 
* *
*
'''

n=int(input('enter number of rows:  '))
for i  in range(n+1,0,-1):
    for j in range(i,1,-1):
        print('*',end=" ")
    print()

'''f)
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @'''

n=int(input('enter number of rows:  '))
for i  in range(n):
    for j in range(n):
        print('@',end=" ")
    print()