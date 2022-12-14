
#1

person = {
    'name': 'Abdal',
    'age': 18,
    'hobbies': ['reading', 'playing games', 'sleeping']
}

print(f" {person['name']} \n {person['age']}")

#2

person['age'] = 0
person['country'] = 'Kuwait'
print(person)
print(len(person))

#3

person['hobbies'].append('designing')

def check_hobbies(person):
    if len(person) >= 3:
        print(' you are amazing')
    
    else: print('try harder')

check_hobbies(person)