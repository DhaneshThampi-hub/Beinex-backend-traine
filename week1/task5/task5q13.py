# a
rows = 4
for i in range(1, rows + 1):
    for k in range(rows, i, -1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# b
number = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()
#c
for i in range(1, rows + 1):
    # Inner loop for repeating numbers in each row
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

#d
for i in range(1, rows + 1):
    # Inner loop for '*' in each row
    for j in range(1, i + 1):
        print("*", end=" ")
    
    print()