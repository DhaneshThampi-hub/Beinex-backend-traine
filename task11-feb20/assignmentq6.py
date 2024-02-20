'''6) Write a Python program to implement a queue using a list.(enqueue and dequeue)'''

queue = []
def enqueue(item):
    queue.append(item)
def dequeue():
    if not is_empty():
        return queue.pop(0)
    else:
        print("Queue is empty")
def is_empty():
    return len(queue) == 0
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Exit")   
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        item = input("Enter the item to enqueue: ")
        enqueue(item)
        print("Queue after enqueuing:", queue)
    elif choice == '2':
        dequeued_item = dequeue()
        if dequeued_item is not None:
            print("Dequeued item:", dequeued_item)
            print("Queue after dequeuing:", queue)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")