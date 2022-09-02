# decimal to binary

dec = int(input("Enter the Decimal: "))        # input decimal
bin_cage = []                                  # insert a blank list

while dec >= 1:                                # Create while loop for as the decimal will turn on in one eventually
    remainder = dec % 2                        # Insert the remainder variable, as the result of zero or 1 in decimal modulo 2 (dec%2)
    bin_cage.append(int(remainder))            # Append the value of the remainder per loop, store the value in int()
    dec = dec/ 2                               # Decimal will eventually turn in one and stop the loop

bin_cage.reverse()                             # After the loop, reverse the lists to indaciate the arrangement of binary
bin_cage_length = len(bin_cage)                # Store the length of the lists into other variable

for i in range (bin_cage_length):              # Create for loop to print the Binary
    print(bin_cage[i], end ='')                # Print the Binary, dont forget the end='' to display it in a column