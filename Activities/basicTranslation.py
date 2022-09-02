'''
Tagalog Language
C --> K
V --> B
F --> P
G --> Dyi
'''

def translate(word):
    translation = ""                                # the final correct translation
    for letter in word:                             # loop, every letter in inserted word
        if letter.lower() in "c":
            if letter.isupper():
                translation += "K" 
            else:
                translation += "k"
        elif letter.lower() in "v":
            if letter.isupper():
                translation += "B" 
            else:
                translation += "b"
        elif letter.lower() in "f":
            if letter.isupper():
                translation += "P" 
            else:
                translation += "p"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))