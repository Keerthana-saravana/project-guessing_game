# project_password_generator_app

import random
import string
def Password_generate(length=12,include_uppercase=True,include_lowercase=True,include_numbers=True,include_special_characters=True):
    #defining the character available for password
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase if include_uppercase else ""
    digits=string.digits if include_numbers else ""
    special=string.punctuation if include_special_characters else ""
    
    #combining all the characters
    all_characters=lower+upper+digits+special
     
    #declaring the value error 
    if not all_characters:
        raise ValueError("any one of the character is must needed to generate the password")
    
    #creating an empty list for password
    password=[]
    
    if include_uppercase:
        password.append(random.choice(upper))
    if include_numbers:
        password.append(random.choice(digits))
    if include_special_characters:
        password.append(random.choice(special))
    password.append(random.choice(lower)) #password must always contains atleast one lower case

    while len(password)<length:
        password.append(random.choice(all_characters))

        #shuffling the password
        random.shuffle(password)

    #joining the all characters in the password without any space 
    return "".join(password)


print("Welcome to my password generator app!!")
name=input("enter your name:")
print(f"Welcome {name} to my password generator app!!")
#getting inputs from the user to generate the password
length=int(input("enter your password length:"))
include_uppercase=input("do you want to include uppercase in your password?(yes/no):").strip().lower()=="yes"
include_numbers=input("do you want to include digits in your password?(yes/no):").strip().lower()=="yes"
include_special_characters=input("do you want to include special characters in your password?(yes/no):").strip().lower()=="yes"

password=Password_generate(length,include_uppercase,include_numbers,include_special_characters)
print("your  generated password is:",password)
result=input("Do you like my password generator?(yes/no):")
if result.lower()=="yes":
    print("Thankyou for your comments!!")
    print("Thanks for using my password generator!!")
else:
    print("oh sorry for this!!,we will try to improve our password generator!!")

    
