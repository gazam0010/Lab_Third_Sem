#Iterate two lists simultaneously one of them in reverse order

lt1 = [1,2,3,4,5,6,7]
lt2 = [9,8,7,6,5,4,3]

length = len(lt1)

for i in range(length):
    print(f"List 1: {lt1[i]} and List 2 (reversed): {lt2[length-i-1]}")
    

