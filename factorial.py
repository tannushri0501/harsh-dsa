number = int(input("Enter a number: "))
result = 1
counter = number

while counter > 1:
    result = result * counter
    counter -= 1

print("Factorial =", result)
