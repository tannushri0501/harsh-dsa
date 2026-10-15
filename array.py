```python
data = [0] * 100
length = int(input("How many elements do you want? "))

for index in range(length):
    data[index] = int(input("Enter element: "))

while True:
    print("\n===== ARRAY OPERATIONS =====")
    print("1. Add an element")
    print("2. Remove an element")
    print("3. Display array")
    print("4. Quit")

    option = int(input("Choose an operation: "))

    match option:
        case 1:
            position = int(input("Enter insertion position: "))
            value = int(input("Enter the new value: "))

            if 1 <= position <= length + 1 and length < 100:
                index = length

                while index >= position:
                    data[index] = data[index - 1]
                    index -= 1

                data[position - 1] = value
                length += 1
                print("New element added successfully")
            else:
                print("Insertion not possible")

        case 2:
            position = int(input("Enter deletion position: "))

            if 1 <= position <= length:
                index = position - 1

                while index < length - 1:
                    data[index] = data[index + 1]
                    index += 1

                length -= 1
                print("Element removed successfully")
            else:
                print("Position is out of range")

        case 3:
            if length == 0:
                print("No elements to display")
            else:
                print("Updated array:", end=" ")
                for index in range(length):
                    print(data[index], end=" ")
                print()

        case 4:
            print("Closing the program")
            break

        case _:
            print("Invalid option. Try again.")
```
