from datetime import datetime

def timeit(arg): # Функция декоратор в качестве переменной аргумента получает на вход нашу функцию которую мы хотим обернуть
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs): # Функция обертка
            start = datetime.now()
            result = func(*args, **kwargs) # Здесь мы вызываем функцию которую мы хотим обернуть через переменную func
            print(datetime.now() - start)
            return result
        return wrapper # Функция timeit будет возвращать функцию wrapper
    return outer
@timeit('name')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0: # Означает "если число i четное"
            l.append(i)
    return l

@timeit('name')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

one(10000)
two(10000)

#l1 = timeit('name')(one)(10000) # Это аналогично написанию wrapper(10000) которая считает результат работы one(10000)