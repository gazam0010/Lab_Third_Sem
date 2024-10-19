#Separate alphabets and numbers form the entered string

s1 = input("Enter a string: ")
alphabets = []
numbers = []

for x in s1:
    try:
        temp = int(x)
        numbers.append(x)
    except ValueError:
        alphabets.append(x)
        
print(f"Alphabets: {alphabets} \nNumbers: {numbers}") 