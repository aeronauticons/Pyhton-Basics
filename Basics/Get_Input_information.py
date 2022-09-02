
#input
#input("Enter Numbers: ")

# storing in variable
num = input("Enter Age: ")
print(num + " year's old!")

# in string
name = input("Name: ")

print("Hello " + name + "! You are " + num + " year's old!")


# build basic calculator (operations)
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
result = int(num1) + int(num2)        # int () or float() --> converts string to numbers
result2 = float(num1) + float(num2)  

print(result, result2) # or print(int(num1) + int(num2))
