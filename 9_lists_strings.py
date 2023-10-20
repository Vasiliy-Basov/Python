# Списки (Lists) [] и строки
# List – это массив или контейнер, который содержит списки на другие объекты,
# к этим объектам можно обратиться по номеру его места которое этот объект
# занимает в списке (от 0 до бесконечности) номера — это индексы.
# Литерал списка []
l = ['a', 'b', 'c', 'd']
print (f'Это наш список: {l}')
print(f'Это первое значение списка l: {l[0]}')
print(f'Узнать индекс последнего элемента: {len(l) - 1}')
print(f'Последний элемент списка: {l[-1]}')
print(f'Предпоследний элемент списка: {l[-2]}')
print(f'Срез списка от индекса 1 до 3 не включая 3, Элементы со 2 до 3: {l[1:3]}')
print(f'Срез списка, начиная с индекса 1 и до конца: {l[1:]}')
print(f'Срез списка, начиная с начала и до индекса -1, не включая его: {l[:-1]}')
print(f'Срез списка, начиная с начала и до индекса -1, не включая его, с шагом 2: {l[:-1:2]}')

# Методы для списков append и extend
# Append – добавляет в конец списка еще один элемент
l.append('e')
print(l)  # -> ['a', 'b', 'c', 'd', 'e']

# Если применим к пустому списку append двух других списков, то общий список будет состоять из списка списков
l2 = [1, 2, 3, 4]
rl = []

rl.append(l)
rl.append(l2)
print(rl)  # -> [['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4]]

# Очистка списка метод clear
rl.clear()

# Что бы получить плоский список нужно использовать extend
rl.extend(l)
rl.extend(l2)
print(rl)  # -> ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4]

rl1 = rl + ['x', 'y', 'z']
print(rl1)

x = 3
y = x
print(y)
print(id(x))
print(id(y))
x = x + 1
print(id(x))
print(id(y))

l = []
new = l
print(id(new))
print(id(l))
new.append('a')
print(new)
print(l)
print(id(new))
print(id(l))
l.append('b')
l.append('m')
l.append('c')

m = ['a', 'b', 'm', 'c']
sl = sorted(m)
print(sl)
print(m)

m.sort()
print(m)

s = 'Знайка шел гулять на речку\nперепрыгнул_через_овечку'
print(s)

s2 = s.split()
print(s2)

l = s.split('\n')
print(l)

l1 = s.replace('_', ' ')
l2 = l1.split()
print(l2, 'l2')

n = ' '
r = n.join(l2)
print(r)

children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Bubnov_2015']
s_children = sorted(children)
print(s_children)


def by_year(name):
    return name.split('_')[-1]


print(by_year(children[0]))
s_children = sorted(children, key=by_year)
print(s_children)
