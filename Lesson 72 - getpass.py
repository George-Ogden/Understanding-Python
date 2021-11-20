from getpass import *

try:
    username = getuser()
except:
    username = input("Enter username: ")

password = getpass("Enter password: ")

print(f"Username: {username}\nPassword: {password}")