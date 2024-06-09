import random
import string

letters = string.ascii_letters
numbers = string.digits
special_char = string.punctuation
all_char = letters + numbers + special_char


while True:
    pwd = input("Enter length of password: ")
    if pwd.isdigit():
        pwd = int(pwd)
        break

password = ''
for i in range(pwd):
    password += random.choice(all_char)
    
    
print("Generated password is", password)
        
    
