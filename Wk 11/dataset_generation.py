import pandas as pd
import numpy as n

gender = ['Male', 'Female']
location = ['Rural', 'Suburban', 'Urban']
age_group = ['18-25', '26-35', '36-45', '46-55', '56+']
x5_values = n.random.uniform(10, 100, 100) #low high
x4_values = n.random.normal(loc=50000, scale=20000, size=100) #meanstdev
x6_values = n.random.randint(0, 12, 100) #random data
y_values = n.random.choice([0, 1], 100)



data_gen = {
    'x1': n.random.choice(gender, 100),
    'x2': n.random.choice(location, 100),
    'x3': n.random.choice(age_group, 100),
    'x4': x4_values,
    'x5': x5_values,
    'x6': x6_values,
    'y': y_values
}

dframes = pd.DataFrame(data_gen)
print(dframes)