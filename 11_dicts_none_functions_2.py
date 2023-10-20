person = {'name': 'vasya', 'surname': 'pupkin', 'email': 'test@gmail.com'}
print(person)

d = dict(name='petr', tel='1234')
print(d)

name = person['name']
print(name)

tel = person.get('tel')
print(tel)

tel = person.get('tel', '1231234')
print(tel)

tel = person.setdefault('tel', '1231256')
print(tel)
print(person)

for item in person.keys():
    print(item)

for item in person.items():
    print(item)

a, b = [1, 2]
print(a)
print(b)

for key, value in person.items():
    print(key, value)

new = {'Gender': 'Male'}
person.update(new)
print(person)


person.update(name='dima', tel='3333')
print(person)


def a():
    print('hello world')
    return None
result = a()
print(result)