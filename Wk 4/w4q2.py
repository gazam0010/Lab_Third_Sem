#Compare first and last term of a list

def compare_first_last(lst):
    if len(lst) <= 2:
        return True
    else:
        return lst[0] == lst[-1]

r = int(input("Enter number of elements in the list: "))

#list_comprehension
lst = [int(input("Enter element: ")) for i in range(r)]

print(compare_first_last(lst))
