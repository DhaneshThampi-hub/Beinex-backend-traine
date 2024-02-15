'''3.Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3'''

list = ['abc', 'xyz', 'aba', '1']
count = 0
for string in list:
    if len(string) >= 2:
        count += 1
print("Sample List:", list)
print("Number of strings with length 2 or more:", count)