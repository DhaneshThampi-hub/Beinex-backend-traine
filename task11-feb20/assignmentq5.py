'''5) Write a Python program to implement a stack using a list.(push and pop)
'''

stack = []
def push(item):
    stack.append(item)
def pop():
    if not is_empty():
        return stack.pop()
    else:
        print("Stack is empty")
def is_empty():
    return len(stack) == 0
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        item = input("Enter the item to push: ")
        push(item)
        print("Stack after pushing:", stack)
    elif choice == '2':
        popped_item = pop()
        if popped_item is not None:
            print("Popped item:", popped_item)
            print("Stack after popping:", stack)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")