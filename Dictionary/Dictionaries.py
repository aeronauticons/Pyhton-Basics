'''
syntax of Dictionary 

variable = {

}
'''


month_conversion = {
    "Jan" : "January",
    "Feb" : "Febuary",
    "Dec" : "December"
}

print(month_conversion["Dec"])
print(month_conversion.get("Jan"))
print(month_conversion.get("Nov"))  # --> none but
print(month_conversion.get("Nov", "not a valid key")) # --> not a valid key