import string

s = input("Enter a String: ")

count_uppercase = sum(1 for char in s if char.isupper())
count_lowercase = sum(1 for char in s if char.islower())
count_digit = sum(1 for char in s if char.isdigit())
total_alpha = count_lowercase + count_uppercase


print(f"Uppercase: {count_uppercase}, Lowercase: {count_lowercase}, Digits: {count_digit} and Total alphabets: {total_alpha}")
