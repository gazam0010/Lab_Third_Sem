#Average salary in each department

import numpy as n
with open('Lab F/Lab_Third_Sem\Wk 7/Employees.txt', 'r') as emp:
    employee_data = [line.strip().split(',') for line in emp]

with open('Lab F/Lab_Third_Sem\Wk 7/Departments.txt', 'r') as dpt:
    department_data = {line.strip().split(',')[0]: line.strip().split(',')[1] for line in dpt}
    
dept_salaries = {}

for e in employee_data:
    did = e[3].strip()
    salary = float(e[2])  
    
    if did not in dept_salaries:
        dept_salaries[did] = []
    dept_salaries[did].append(salary)  

for did, salary in dept_salaries.items():
    mean = n.mean(salary)  
    print(f"Department: {department_data[did]} and Average salary: {mean}")