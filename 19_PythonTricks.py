a = 2
b = 1
a, b = b, a
print(a, b)


def test(x,y,z):
    print(x,y,z)

l = [1, 2, 3]
d = {'x': 1, 'y': 2, 'z': 3}

test(*l)
test(**d)

# lambda это анонимная функция которая принимает
# два аргумента x,y и выдает сумму и разность.
d = {'sum': lambda x,y: x + y,
     'sub': lambda x,y: x - y}

print(d['sum'](1,2))
print(d['sub'](1,2))