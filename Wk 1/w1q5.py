#Find sum of digits of a supplied integer

num = int(input("Enter a number: "))

sum = 0

while (num > 0):
    digit = int(num % 10)
    sum = sum + digit
    num = num // 10

print(sum)