# Count maximum occurence of a character

import string

with open('Wk 9/random_text.txt', 'r') as file:
    text = file.read()

text = text.lower()

alphabets = string.ascii_lowercase

count = 0
max_count = 0
max_alpha = ''

for alphabet in alphabets:
    count = text.count(alphabet)
    
    if count > max_count:
        max_count = count
        max_alpha = alphabet

print(f"Alphabet having maximum occurences is: '{max_alpha}' occuring {count} times.")