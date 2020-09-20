#!python3
import random
from string import punctuation
from string import digits
from string import ascii_uppercase, ascii_lowercase
import pyperclip
import pickle


def passwordGenerator(num):
    combined_list = punctuation + digits + ascii_uppercase + ascii_lowercase
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(combined_list) for i in range(num))
    pyperclip.copy(password)
    print("Password copied successfully")

def checkLength(num):
    if num < 8:
        print("Please enter digit greater than 8\n")
    else:
        passwordGenerator(num)
        

        
if __name__ == "__main__":
    
    num = int(input("How many digits of password you want : "))
    checkLength(num)

