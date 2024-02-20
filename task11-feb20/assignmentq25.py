'''25) Write a Python program to count the number of occurrences of each element in a tuple'''

def count_occurrences(input_tuple):
    occurrences = {}
    for element in input_tuple:
        occurrences[element] = occurrences.get(element, 0) + 1
    return occurrences
input = input("Enter elements of the tuple separated by spaces: ")
tuple = tuple(map(int, input.split()))
result = count_occurrences(tuple)
print(result)


