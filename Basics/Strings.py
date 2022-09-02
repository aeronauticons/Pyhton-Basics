bachelor = "Bachelor of Science"
inWhat = "in Mathematics"
major = "with Specialization in Computer Science"

print ("1. " + bachelor + " in Mathematics with Specialization in Computer Science")
#or
Course = bachelor + " " + inWhat + " " + major

#awsome stuff

#upper and lower case
print("2. " + Course.lower())
print("3. " + Course.upper())

#checking if upper or lower case
print(Course.islower())
print(Course.isupper())

#combinatiom
print(Course.upper().isupper())
print(Course.lower().islower())

#length function
print(len(Course)) #74 char

#individual Char
print(Course[0])
print(Course[5], Course[0].lower(), Course[23].lower())
print(Course[23:34])

#detecting letter index
print(Course.index("C"))

#replace
print(Course.replace("in Computer Science", "in Applied Statistics"))