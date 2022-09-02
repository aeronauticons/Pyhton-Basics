# lists or arrays
fav_Subjects = ["Calculus", "Trigonometry", "Algebra"] #strings
num_Units = [3.0, 5.0, 3.0] #int floats
isGoodSubject = [True, False] #boolean

#print
print(fav_Subjects)
print(num_Units)
print(isGoodSubject)

#from index
print(fav_Subjects[2] + " is " + str(num_Units[2]) + " units. And it is not my favorite one!")

# index to index
print(fav_Subjects[0:2]) # not include the last index

#modify
fav_Subjects[2] = "Linear Algebra"
print(fav_Subjects[2])

# Lists Function
# 1. Extend (Allow to append other lists)
fav_Subjects.extend(num_Units)
print(fav_Subjects)

# 2. Append (add in the final index a new item)
num_Units.append("2.0")
print(num_Units)

# 3. Insert  (index, position)
num_Units.insert(0, 1.0)
print(num_Units)

# 4. Remove 
fav_Subjects.remove(3.0)
fav_Subjects.remove(5.0)
fav_Subjects.remove(3.0)
print(fav_Subjects)

# 5. Remove all
isGoodSubject.clear()
print(isGoodSubject)

# 6. Pop (remove last Item)
num_Units.pop()
print(num_Units)

# Detecting index by typing keyword
print(fav_Subjects.index("Calculus"))

#count how many time that values repated
print(num_Units.count(3.0))

# sort assending(default) and descending
fav_Subjects.sort()
num_Units.reverse()
print(fav_Subjects)
print(num_Units)


#copying lists
favsubj = fav_Subjects.copy()
print(favsubj)