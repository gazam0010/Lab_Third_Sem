#Void function to add the square of first two and last two digits of a number

def void_function (num):
    num_str = str(num)
    first_half = int(num_str[:2])
    second_half = int(num_str[2:])
    
    result = (first_half * first_half)  + (second_half * second_half)
    print(result)

void_function(1100)