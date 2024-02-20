'''4) Write a Python program to perform matrix multiplication using lists of lists'''


p = []
rows_p = int(input("Enter the number of rows for matrix 1: "))
cols_p = int(input("Enter the number of columns for matrix 1: "))
for i in range(rows_p):
    linear1 = []
    for j in range(cols_p):
        k = int(input("Enter the element for matrix 1: "))
        linear1.append(k)
    p.append(linear1)


for i in range(rows_p):
    for j in range(cols_p):
        print(p[i][j], end=' ')
    print()


l = []
rows_l = int(input("Enter the number of rows for matrix 2: "))
cols_l = int(input("Enter the number of columns for matrix 2: "))
for i in range(rows_l):
    linear2 = []
    for j in range(cols_l):
        k = int(input("Enter the element for matrix 2: "))
        linear2.append(k)
    l.append(linear2)

for i in range(rows_l):
    for j in range(cols_l):
        print(l[i][j], end=' ')
    print()

if cols_p != rows_l:
    print('metrix cannot multiplied length of two matrix must be same!!')
else:
    m = []
    for i in range(rows_p):
        linear3 = []
        for j in range(cols_l):
            linear3.append(0)
        m.append(linear3)

    for i in range(rows_p):
        for j in range(cols_l):
            for k in range(cols_p):  
                m[i][j] = m[i][j] + p[i][k] * l[k][j]

    print("Result of matrix multiplication:")
    for i in range(rows_p):
        for j in range(cols_l):
            print(m[i][j], end=" ")
        print(" ")