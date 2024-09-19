#Create a telephone directory and search a telephone number for provided user

telephone_directory = {}

print("Enter data.")

for _ in range(3):
    name = input("Enter name: ")
    telephone_number = input("Enter telephone number: ")
    telephone_directory[name] = telephone_number

searched_name = input("Enter a name to be searched: ")
if searched_name in telephone_directory:
    result = telephone_directory[searched_name]
    print(f"Telephone number of {searched_name} is {result}")
else:
    print(f"No telephone number found for {searched_name}")
    