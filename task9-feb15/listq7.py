'''7. Write a Python program to find the repeated items of a tuple.'''


tuple = (3, 5, 2, 7, 3, 8, 5, 9, 2, 1)
repeated_items = []
for item in tuple:
    if tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("Repeated items:", repeated_items)