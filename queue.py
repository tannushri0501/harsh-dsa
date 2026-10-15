```python
items = [0] * 5
start = -1
end = -1
MAX = 5

while True:
    print("\n===== QUEUE OPERATIONS =====")
    print("1. Insert element")
    print("2. Remove element")
    print("3. View front element")
    print("4. Show queue")
    print("5. Stop")

    option = int(input("Select an option: "))

    match option:
        case 1:
            if end == MAX - 1:
                print("Queue is full")
            else:
                value = int(input("Enter value: "))

                if start == -1:
                    start = 0

                end = end + 1
                items[end] = value
                print("Value added to queue")

        case 2:
            if start == -1:
                print("Queue is empty")
            else:
                removed = items[start]
                print("Removed value:", removed)

                start += 1

                if start > end:
                    start = end = -1

        case 3:
            if start == -1:
                print("No element available")
            else:
                print("First element:", items[start])

        case 4:
            if start == -1:
                print("Nothing to display")
            else:
                print("Queue contents:", end=" ")
                index = start

                while index <= end:
                    print(items[index], end=" ")
                    index += 1

                print()

        case 5:
            print("Queue program closed")
            break

        case _:
            print("Invalid selection")
```
