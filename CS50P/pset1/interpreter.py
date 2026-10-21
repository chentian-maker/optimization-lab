
expression = input("Expression: ")

x, operator, y = expression.split()

x = float(x)
y = float(y)

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    print(x / y)
