import random


Capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
punctuation = ",.?!"
special_characters = "!@#$%&*()`~"

#I have added this because some sites require a specific minimum length for a password which could differ and i also dont want the password to be a 100 letters
length = int(input("Enter the length for password  "))
password = ""

for i in range(length+1):
    password += random.choice(Capital_letters + Small_letters + numbers + punctuation + special_characters)
print(password)

# I've divided them into seperate categories so that while generating a random password you have atleast one of every type of character because some sites require it
