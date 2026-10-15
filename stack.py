```python
values = [0] * 5
pointer = -1
MAX = 5

while True:
    print("\n===== STACK OPERATIONS =====")
    print("1. Insert (Push)")
    print("2. Remove (Pop)")
    print("3. Show Top")
    print("4. Display Stack")
    print("5. Quit")

    option = int(input("Choose an operation: "))

    match option:
        case 1:
            if pointer >= MAX - 1:
                print("Cannot push: Stack is full")
            else:
                num = int(input("Enter value to push: "))
                pointer += 1
                values[pointer] = num
                print("Value added to stack")

        case 2:
            if pointer == -1:
                print("Cannot pop: Stack is empty")
            else:
                deleted = values[pointer]
                print("Popped value:", deleted)
                pointer -= 1

        case 3:
            if pointer == -1:
                print("Stack has no elements")
            else:
                print("Current top value:", values[pointer])

        case 4:
            if pointer == -1:
                print("Stack is empty")
            else:
                print("Stack from top to bottom:")
                index = pointer

                while index >= 0:
                    print(values[index])
                    index -= 1

        case 5:
            print("Exiting stack program")
            break

        case _:
            print("Invalid option. Please try again.")
```
