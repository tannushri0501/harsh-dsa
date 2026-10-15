deque = [0] * 5
front = -1
rear = -1
MAX = 5

while True:
    print("\n===== DEQUE OPERATIONS =====")
    print("1. Add Element at Front")
    print("2. Add Element at Rear")
    print("3. Remove Element from Front")
    print("4. Remove Element from Rear")
    print("5. Show Deque")
    print("6. Stop Program")

    choice = int(input("Select an option: "))

    match choice:
        case 1:
            if rear == MAX - 1:
                print("Cannot insert: Deque is full")
            else:
                value = int(input("Enter value to insert: "))

                if front == -1:
                    front = rear = 0
                else:
                    for i in range(rear, front - 1, -1):
                        deque[i + 1] = deque[i]
                    rear += 1

                deque[front] = value
                print("Element added at the front successfully")

        case 2:
            if rear == MAX - 1:
                print("Cannot insert: Deque is full")
            else:
                value = int(input("Enter value to insert: "))

                if front == -1:
                    front = rear = 0
                else:
                    rear = rear + 1

                deque[rear] = value
                print("Element added at the rear successfully")

        case 3:
            if front == -1:
                print("Cannot delete: Deque is empty")
            else:
                removed = deque[front]
                print("Removed element:", removed)

                if front == rear:
                    front = rear = -1
                else:
                    front += 1

        case 4:
            if front == -1:
                print("Cannot delete: Deque is empty")
            else:
                removed = deque[rear]
                print("Removed element:", removed)

                if front == rear:
                    front = rear = -1
                else:
                    rear -= 1

        case 5:
            if front == -1:
                print("Deque contains no elements")
            else:
                print("Current deque:", end=" ")
                index = front

                while index <= rear:
                    print(deque[index], end=" ")
                    index += 1
                print()

        case 6:
            print("Exiting deque operations...")
            break

        case _:
            print("Please select a valid option")
