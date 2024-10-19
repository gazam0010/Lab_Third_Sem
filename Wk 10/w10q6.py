with open('Wk 10/q6Employees.txt', 'r') as emp, open('Wk 10\q6Departments.txt', 'r') as dep:
    
    employee_data = {}
    for line in emp:
        fields = line.split(',')
        emp_did = fields[3].strip()
        
        if emp_did not in employee_data:
            employee_data[emp_did] = []
        employee_data[emp_did].append(fields[:3])
    
    department_data = {}
    for line in dep:
        fields = line.split(',')
        dep_did = fields[0].strip()
        department_data[dep_did] = fields[1:]
        
    merged_data = []
    for did, employees in employee_data.items():
        dep_info = department_data[did]
        for emp_info in employees:
            merged_data.append(emp_info + [did] + dep_info)
            
with open('Wk 10/q6Merged.txt', 'w') as merged:
    for row in merged_data:
        merged.write(','.join(row) + '\n')

