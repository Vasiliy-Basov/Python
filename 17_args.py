def add(a,b):
    print(a + b)
add(2,3)

def add1(*args):
    print(args)
    print(sum(args))

l = [1,2,3]
add1(*l)

def add2(a, *args):
    print(a)
    print(args)
    print(sum(args))

l = [1,2,3]
add2(*l)

def gen():
    for i in range(1,10):
        yield i
def add3(*args):
    print(args)
    print(sum(args))

add3(*gen())

def add4(*args, **kwargs):
    print(args)
    print(kwargs)

l = [1,2,3]
add4(*l, street='lenina', house=12)

def add5(l, **kwargs):
    print(l)
    print(kwargs)

l = [1,2,3]
add5(l, street='lenina', house=12)