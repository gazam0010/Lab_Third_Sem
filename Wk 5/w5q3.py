#Generate a password of length 10, having atleast 2 uppercase, 1 punctuation and 1 digit

import string
import random

set_of_uppercase = string.ascii_uppercase
set_of_lowercase = string.ascii_lowercase
set_of_punctuations = string.punctuation
set_of_digits = string.digits

range_of_uppercase = random.randint(2,8)

password = [random.choice(set_of_uppercase) for i in range(range_of_uppercase)]

password.append(random.choice(set_of_digits))
password.append(random.choice(set_of_punctuations))

remaining_len_pass = 10 - len(password)

while remaining_len_pass > 0:
    password.append(random.choice(set_of_lowercase))
    remaining_len_pass -= 1

random.shuffle(password)

final_password = ''.join(password)

print(final_password)