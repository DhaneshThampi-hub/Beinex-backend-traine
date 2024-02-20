'''8) Write a Python program to reverse a list'''

def rev_list(list):
    reversed_list=[]
    for i in range(len(list)-1,-1,-1):
        reversed_list.append(list[i])
    return reversed_list
a=input("enter a numbers to add in a list: ")
list = [int(num) for num in a.split(',')]
reversed_result = rev_list(list)
print("Reversed list:", reversed_result)




