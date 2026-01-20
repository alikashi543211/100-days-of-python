import random

def random_3_chars():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(letters) for _ in range(3))

message  = input("Enter your message to encrypt: ")
if(len(message) == 2):
    encrypted_message = message[1] + message[0]
elif(len(message) > 2):
    encrypted_message = message[len(message)-1] + random_3_chars() + message[1:(len(message)-1)] + random_3_chars() + message[0]

print("Encrypted Message: " + encrypted_message)

message = input("Enter your message to Decrypt: ")

if(len(message) == 2):
    decrypted_message = message[1] + message[0]
elif(len(message) > 2):
    decrypted_message = message[len(message)-1] + message[4:len(message)-4] + message[0]

print("Decrypted Message : " + decrypted_message)