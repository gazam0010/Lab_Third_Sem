#Print supplied char from the user

def removeChar(name, n):
    return name[:n]

name = input("Enter your name: ")
n = int(input("Number of chars: "))

print(removeChar(name, n))