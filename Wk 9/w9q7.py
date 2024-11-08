# Calculate and add HRA as a new column in each entry

with open('Lab F/Lab_Third_Sem/Wk 9/employees_data.txt', 'r+') as file:
    lines = file.readlines()
    updated_line = []
    
    for line in lines:
        hra = 18/100 * int(line.split(',')[2])
        updated_line += [line.strip() + f',{hra}\n']
        
    file.seek(0)
    
    file.writelines(updated_line)