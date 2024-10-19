#Count the occurences of each vowel in the text file

with open('Wk 8/vowelsFile.txt', 'r') as file:
    data = file.read()

data = ''.join(data.split())

vowels = ['a','e','i','o','u','A','E','I','O','U']

count = 0

for vowel in vowels:
    count = data.count(vowel)
    print(f"Vowel '{vowel}' found {count} times!")