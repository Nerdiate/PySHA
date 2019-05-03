import uuid
import hashlib

print ("Welcome to PySHA, a text based hash creator! ")
print ("Version 1.0.0")
print ("            ")
print ("Unfortunately, only SHA-1 160 byte is available for right now, make sure to look out for newer versions.")
print ("         ")

def hash_password(password):
    # uuid is used to generate a random number
    spice = uuid.uuid4().hex
    return hashlib.sha1(spice.encode() + password.encode()).hexdigest() + ':' + spice


def check_password(hashed_password, user_password):
    password, spice = hashed_password.split(':')
    return password == hashlib.sha1(spice.encode() + user_password.encode()).hexdigest()


new_pass = input('Enter the string you wish to have hashed: ')
hashed_password = hash_password(new_pass)
print('Your hashed string: ' + hashed_password)

with open("passhex.txt", "a") as f:
    f.write(new_pass + '\n')
    f.write(hashed_password + '\n')
    f.write('_____________________________________________________________________________________' + '\n')
