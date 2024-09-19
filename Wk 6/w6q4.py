#Ecrypt and decrypt an string

import string
import random

set_of_punctuations = string.punctuation
def encypt(s):
    encypted_string = ""
    for char in s:
        random_punctuation = random.choice(set_of_punctuations)
        
        encypted_string += char + random_punctuation
        
    return encypted_string
def decrypt(e):
    decypted_string = ""
    
    for i in range(0, len(e), 2):
        decypted_string += e[i]
    
    return decypted_string

choice = input("Enter 'e' to ecrypt and 'd' to decrypt: ")
print()
string = input("Enter your string: ")

if choice == 'e':
    print(encypt(string))
elif choice == 'd':
    print(decrypt(string))
else:
    print("Invalid choice")
    
    
   