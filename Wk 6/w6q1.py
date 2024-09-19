#Take input and join two tuples

print("Enter data for first tuple.")

tp1 = tuple((int(input("Data: ")) for x in range(3)))

print("Enter data for second tuple.")

tp2 = tuple((int(input("Data: ")) for x in range(2)))

tp3 = tp1 + tp2
print(tp3)
