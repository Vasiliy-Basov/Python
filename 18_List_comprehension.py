jack = {
    'name': 'jack',
    'car': 'bmw'
}

john = {
    'name': 'john',
    'car': 'audi'
}


users = [jack, john] # это список словарей

cars = [person.get('car', '') for person in users]
print(cars)

cars = []
for person in users:
    cars.append(person['car'])
print(cars)

names = ['jack', 'john', 'oleg', 'ula']
new_names = [n for n in names if n.startswith('j')]
print(new_names)

new_names = []
for n in names:
    if n.startswith('j'):
        new_names.append(n)

print(new_names)