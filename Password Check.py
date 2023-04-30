import re

password = input("Enter Your Password: ")

#def password_strength(password):

if len(password) < 6:
    print("Weak Password")
elif len(password) >= 8 and not re.search('[^A-Za-z0-9]', password):
    print("Moderate Password")
elif len(password) >= 8 and re.search('[^A-Za-z0-9]', password) and re.search('[0-9]', password) and re.search('[A-Z]', password) and re.search('[a-z]', password):
    print("Strong Password")
else:
    print("Moderate Password")

 






