num = int(input("Enter a number: "))

while (num > 0):
    digit = int(num % 10)
    print(digit)
    num = num // 10
    