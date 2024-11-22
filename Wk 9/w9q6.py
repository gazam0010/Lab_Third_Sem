# Count number of subjects against each course

with open('Lab_Third_Sem\Wk 9\Course Structure.txt', 'r') as file:
    data = [line.strip().split(',')[0] for line in file]

courses = set(data)

for course in courses:
    print(f'{course} - {data.count(course)}')