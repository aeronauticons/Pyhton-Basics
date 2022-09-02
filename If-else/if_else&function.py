#combination of function and if-else

def biggest_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(biggest_num(100, 2000, 123))


# compare strings (==) --> equals, (!=) --> not equals
pet = input("Input a pet that you love: ")

if pet == "dogs" or pet =="Dogs" or pet == "DOGS":
    print("Yes its a Good Dog!")
elif pet == "cat" or pet == "Cat" or pet == "CAT":
    print("Wow amazing cat!")
elif pet.lower() == "hamster":
    print("Ow! So beautiful small hamster!")
else:
    print("Maybe that is not a pet!")