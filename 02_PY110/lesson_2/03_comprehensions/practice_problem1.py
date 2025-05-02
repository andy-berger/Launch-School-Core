munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_male_age = 0
for info in munsters.values():
    if info['gender'] == 'male':
        total_male_age += info['age']

print(total_male_age)

total_male_age = sum({monster['age'] for monster in munsters.values() if monster['gender'] == 'male'})

print(total_male_age)