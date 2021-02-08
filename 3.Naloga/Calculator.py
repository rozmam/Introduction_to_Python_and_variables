x = float(input("Write number for X: "))

y = float(input("Write number for Y: "))

artithmetic_operation = input("Please enter one of those arithmetic operation (`+`, `-`, `*`, `/`): ")

if artithmetic_operation == "+":
    print(x + y)
elif artithmetic_operation == "-":
    print(x - y)
elif artithmetic_operation == "*":
    print(x * y)
elif artithmetic_operation == "/":
    print(x / y)
else:
    print("Something went wrong.")