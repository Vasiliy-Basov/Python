# filter(func, iterable)
def has_o(string):
    return 'o' in string.lower()

l = ['one', 'two', 'three', '23Fkdfd']
nl = list(filter(has_o, l))
print(nl)

newl = list(filter(lambda string: 'o' in string.lower(), l))
print(newl)

nl_gen = [string for string in l if has_o(string)]
print(nl_gen)