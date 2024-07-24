print("Calculator")
print("Enter the first number:")
a = int(input())
print("Enter the second number:")
b = int(input())

print("Select operation:")
print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
c = int(input())

if c == 1:
    print("Result:", a + b)
elif c == 2:
    print("Result:", a - b)
elif c == 3:
    print("Result:", a * b)
elif c == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
elif c == 5:
    print("Exit")
else:
    print("Invalid selection, exiting.")




