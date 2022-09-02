# read - r
# write - w
# append - a
# read and write - r+

quotes = open("quotes.txt", "r")
tryprog = open("Try&Except.py", "r")

#print(quotes.readable())              # detects if it is readable or not [Boolean result]
#print(quotes.read())                  # spit outs the text in txt file

#print(quotes.readline())             # read the first line until the last line you've entered
#print(quotes.readline())
 

#print(quotes.readlines())            # coinside all sentence line in an array
#print(tryprog.readlines()[0])    

# inserting the readlines into loop

i=0
for quote in quotes.readlines():
    i += 1
    print(str(i) + ". " + quote)

quotes.close()                        # closing the file
tryprog.close()    