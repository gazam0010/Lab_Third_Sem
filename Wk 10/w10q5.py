# Count maximum occurence of a character then replace it with the word Aligarh

with open('Wk 10/forq5.txt', 'r+') as file:
    data = file.read()

    words = data.lower().split()

    count = 0
    max_count = 0
    max_word = ''

    for word in words:
        count = data.count(word)
        
        if count > max_count:
            max_count = count
            max_word = word

    new_data = data.replace(max_word, 'Aligarh')
    
    file.seek(0)
    
    file.writelines(new_data)