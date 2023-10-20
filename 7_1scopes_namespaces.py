# Пространство имен(Namespace), область видимости(Scope)
# Пространство имен(Namespace) – это словарь {} вызывается функцией locals()

# Функция locals() – Это функция которая возвращает нам словарь {}
# в которой перечислены имена локальных переменных и их значения.
def a():
    name = 'Pupkin'
    age = 12
    print(locals())


a()  # -> {'name': 'Pupkin', 'age': 12}

# Функция для сравнения пространств имен(Namespace) locals() внутри функции и снаружи
name = 'Eroha'


def a():
    name = 'Pupkin'
    age = 12
    print('Function a() namespace:', locals())


# Мы видим содержание наших разных namespace в том числе в глобальном (External)
# словаре имени 'a' присвоен объект функции
print('External namespace:',
      locals())  # -> External namespace: {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001CD1B594850>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__':
# 'D:\\Dropbox\\Python\\Learn\\7_1scopes_namespaces.py', '__cached__': None, 'a': <function a at 0x000001CD1B5EED40>,
# 'name': 'Eroha'}
a()  # Function a() namespace: {'name': 'Pupkin', 'age': 12}


# Scope – область видимости
# Порядок поиска в пространствах имен
# Locals – локальное пространство имен
# Enclosed – пространство имен которое выше на ступень чем локальное но еще не глобальное (функция внутри функции)
# Global – глобальное пространство имен
# Built-ins – уровень модуля built- ins который неявно импортируется
# при запуске интерпретатора и который содержит все встроенные типы и функции.

# Всякий раз, когда мы объявляем функцию или другой блок мы создаем пространство имен (словарь с именами и значениями)
# и область видимости (цепочка пространств имен которая начинается от локального и длится до глобального или built-ins(встроенного) уровня)

def a():
    name = 'in a()'

    def b():
        name = 'Pupkin'
        print(name)  # -> Pupkin
        print(locals())  # -> {'name': 'Pupkin'}

    b()

    print(locals())  # -> {'name': 'in a()', 'b': <function a.<locals>.b at 0x000001ABFD1EED40>}
a()
