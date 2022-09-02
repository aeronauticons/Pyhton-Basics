# read - r
# write - w
# append - a
# read and write - r+


'''quote = open("Read,write/quotes.txt", "a")         # append in the last line in file

quote.write("\nHe's adopted - Thor")

quote.close()'''


'''quote = open("Read,write/quotes.txt", "w")          # override all the text in file

quote.write("\nI assured you borther ... The sun will shine on us again - Loki")

quote.close()'''


quote = open("Read,write/quotes1.txt", "w")          # create new file

quote.write("\nI assured you borther ... The sun will shine on us again - Loki")

quote.close()
