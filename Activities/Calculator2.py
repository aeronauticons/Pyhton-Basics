# all operations

num1 = float(input("Enter 1st number: "))
op =  input("Input Operator: ")
num2 = float(input("Enter 2nd number: "))

if op == "+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid!")