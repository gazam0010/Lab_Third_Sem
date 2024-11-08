# Separate the data in two lists first list having more data than the second list

master_list = list(map(int, input("Enter a list of numbers in even length comma separated: ").split(",")))
length = len(master_list)  

master_list.sort()
half_length = len(master_list) // 2

l1 = master_list[:half_length + 1]
l2 = master_list[half_length + 1:]

print(l1 ," ", l2)
