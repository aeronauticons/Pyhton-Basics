'''
basic if statement in computing GPA if a person is eligible for latin honors!
different syntax from other language
if statement comparisons
'''

exam = input("Enter your exam grade: ")
caps = input("Enter your capstone thesis grade: ")
attend = input("Enter your attendance grade: ")

GPA = (float(exam) + float(caps) + float(attend)) / 3

exam1 = float(exam)
caps1 = float(caps) 
attend1 = float(attend)

if GPA <= 1.75 and GPA >= 1.50:
    if exam1 <= 2.50 and caps1 <= 2.50 and attend1 <=2.50:
        print("Your GPA is " + str(GPA) + ". And your are eligible for Cum Laude")
    else:
        print("Sorry but your Grades is not eligible for Latin Honors")
elif GPA <= 1.49 and GPA >= 1.25:
    if exam1 <= 2.25 and caps1 <= 2.25 and attend1 <= 2.25:
        print("Your GPA is " + str(GPA) + ". And your are eligible for Magna Cum Laude")
    else:
        print("Sorry but your Grades is not eligible for Latin Honors")
elif GPA <= 1.24 and GPA >= 1.00:
    if exam1 <= 2.00 and caps1 <= 2.00 and attend1 <=2.00:
        print("Your GPA is " + str(GPA) + ". And your are eligible for Suma Cum Laude")
    else:
        print("Sorry but your Grades is not eligible for Latin Honors")
else:
    print("Sorry but the " + str(GPA) + " GPA is not eligible for Latin Honors")
