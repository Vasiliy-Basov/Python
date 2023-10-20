# Строки и проверка того что a, a = a.upper() и b = a.upper() это разные объекты.
# Эта особенность строк вынуждает нас каждый раз сохранять операции над строками в новую переменную

a = 'Hello'  # '' - это строка (string)
print(dir(a))  # функция dir получаем все доступные нам аттрибуты строкового типа
a.upper()  # получаем HELLO
id(a)
print(id(a))  # получаем id
b = a.upper()
print(id(b))
a = a.upper()
print(id(a))
print(a)
print(b)

# Метод format.
# Подставляет в фигурные скобки значение переменной
name = 'World'
s = 'Hello {}'
result = s.format(name)
print(result)  # -> Hello World

# Порядок передачи аргументов в метод format имеет значение
name = 'Leon'
number = 100
pattern = '{} - {}'
result = pattern.format(name, number)
print(result)  # -> Leon - 100

# Именованные аргументы
name = 'Leon'
number = 100
pattern = '{movie} - {rating}'
result = pattern.format(movie=name, rating=number)
print(result)  # -> Leon - 100

# F string нотация появилась в python начиная с версии 3.6, не вызываем метод format:
name = 'Leon'
number = 100
result = f'{name} - {number}'
print(result)  # -> Leon - 100
