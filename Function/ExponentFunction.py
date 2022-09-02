#exponents
print(2**3)  #2^3

#creating function

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result

base = int(input("Enter the Base: "))
power = int(input("Enter the Power: "))

print(raise_to_power(base,power))

