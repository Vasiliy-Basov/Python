a = 1
b = a
print(b)
print(id(a))
print(id(b))
a = 2
print(b)
print(id(a))
# Объект b остался старым объект a изменился.

del(a,b)
a = []
b = a
a.append('asdf')
print(b)

def f():
    x = 1
#print(x)

def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner
o = one()
print(o)
print(o())
print(o.__closure__)
print(dir(o.__closure__[0]))
print(o.__closure__[0].cell_contents)
a = o.__closure__[0].cell_contents
print(id(a))
a.append('asdf')
print(o())