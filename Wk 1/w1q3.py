#Print only divisible by 5 in a list

print("Enter 20 numbers in a list.")

lst = []

for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    lst.append(num)

for i in lst:
    if i % 5 == 0:
        print(i, end=" ")

