# square
from math import factorial


stars = int(input("Enter number: "))

print("\nSquare/Rectangle")
for row in range(0, stars):                    # define rows
    for column in range(0, stars):             # define columns
        print("* ", end="")                    # print star + space
    print()                                    # enter new line

# half traiangle
print("\nHalf Triangle")
for rows in range (stars):                     # define rows
    for column in range(rows+1):               # define columns, rows + 1 (so every column the stars add up + 1)
        print("* ", end="")                    # print star + space
    print()                                    # enter new line

# inverted half traiangle
print("\nInverted Half Triangle")
for rows in range(stars):
    for column in range(stars-rows):          # define columns, stars - rows (start printing the star in defined number)
        print("* ", end = "")
    print()

# Mirrored half traiangle
print("\nMirrored Half Triangle")
for rows in range(stars):
    for column in range(stars-rows):
        print(" ", end ="")
    for star_symbol in range(rows+1):
        print(star_symbol, end="")
    print()

# Mirrored inverted half traiangle
print("\nMirrored inverted Half Triangle")
for rows in range(stars):
    for columns in range(rows):
        print(" ", end="")
    for spacing in range(stars -rows):
        print(spacing, end="")
    print()

#diamond
print("\nDiamond")
for rows in range(stars):
    for columns in range(stars-rows):
        print(" ", end = "")
    for star_symb in range(rows+1):
        print("* ", end= "")
    print()

for mid in range(stars+1):
    print("* ", end="")
print()

for rows in range(stars):
    for column in range(rows+1):
        print(" ", end="")
    for spacing in range(stars-rows):
        print("* ", end="")
    print()


# Pascal triangle
print("\nPascal Triangle")
for rows in range(stars):
    for columns in range (stars-rows):
        print(" ", end ="")
    for numbers in range(rows+1):
        print(factorial(rows)//(factorial(numbers)*factorial(rows-numbers)) , end=" ")  # nCr formula
    print() 
        


