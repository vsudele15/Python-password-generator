#This program generates a password according to the inputs of the user
#importing random and string modules
import random
import string

#the function that is responsible to generate the password
def generate_password(min_length, number=True, special_characters=True):
    letters= string.ascii_letters
    digits= string.digits
    special= string.punctuation

    characters= letters
    if number:
        characters += digits
    if special_characters:
        characters += special

    pwd=""
    have_number= False
    have_special= False
    meets_criteria= False

    while not meets_criteria or len(pwd)< min_length:
        new_char= random.choice(characters)
        pwd += new_char
        if new_char in digits:
            have_number=True
        elif new_char in special:
            have_special=True
        
        meets_criteria=True
        if number:
            meets_criteria= have_number
        if special_characters:
            meets_criteria= meets_criteria and have_special
        
    return pwd


min_length= int( input("Enter the minimum length of the password: "))
has_number= input("Enter if you want a number in your password(y/n): ").lower()=="y"
has_special= input("Enter if you want a special character in your password(y/n): ").lower()=="y"

pwd=generate_password(min_length, has_number, has_special)
print(pwd)


