# map(func, *iterable)

def upper(string):
    return string.upper()

l = ['one', 'two', 'three']
new_list = list(map(upper, l))
print(new_list)

def map(func, iterable):
    for i in iterable:
        yield func(i)

# Функция lambda - анонимная функция
new_l = list(map(lambda string: string.upper(), l))
print(new_l)

nl = [string.upper() for string in l]
print(nl)