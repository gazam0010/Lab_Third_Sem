#Print odd and even numbers from first and second list resp.

lt1 = [3,432,32,4,5,1,10,23]
lt2 = [43,53,1,44,23,56,54,3,6]

length_lt1 = len(lt1)
length_lt2 = len(lt2)

#list_comprehension
odd_list = [lt1[i] for i in range(length_lt1) if (lt1[i] % 2 != 0)]
even_list = [lt2[i] for i in range(length_lt1) if (lt2[i] % 2 == 0)]

print(f"Odd list from the first list: {odd_list}")
print(f"Even list from the second list: {even_list}")
