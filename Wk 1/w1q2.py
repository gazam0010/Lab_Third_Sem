num = int(input("Enter a number: "))

count = 0

while (num > 0):
    digit = int(num % 10)
    count += 1
    num = num // 10                