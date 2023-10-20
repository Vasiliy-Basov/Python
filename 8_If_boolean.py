# == - означает равно
# != - означает не равно
# <= - означает меньше либо равно
# >= - означает больше либо равно
# Not – отрицание, not True -> False
# And – и
# Or – или
# += - Прибавит значение правого операнда к левому и присвоит эту сумму левому операнду.
#
# Как true python интерпретирует все не пустые объекты:
# 1)	числа отличные от нуля и все что при вычислении даст не 0
# 2)	не пустые строки
# 3)	не пустые списки и словари
# Как false python интерпретирует все пустые объекты
a = False
if 2 * 2 == 4:  # т.е. если выражение верное
    print('Ok')
else:
    print('not ok')

# Проверяем совпадает ли password и user_input
password = '123'
user_input = ''
if (user_input == password) and (2 * 2 == 4):
    print('Welcome')
else:
    print('Wrong password')

# Это выражение проверяет, содержит ли строка 'Pupkin' символ 'a'
if 'a' in 'Pupkin':  # 'a' нету в 'pupkin' значит false
    print('Welcome')
else:
    print('Wrong password')

# Elif (else if) – последовательные проверки т.е. если одно то пишем одно действие
# если другое то пишем другое действие если третье то третье:
s = '12345678'
if len(s) == 8:
    print('Length 8')
elif len(s) == 6:
    print('Length 6')
else:
    print('not 6,8')

# или для python  3.10 и выше match case:
match len(s):
    case 8:
        print('Length 8')
    case 6:
        print('Length 6')
    case _:
        print('not 6,8')

# Вложенные инструкции if
# Например, нужно проверить, а ввел ли пользователь вообще хоть что-нибудь (пароль):
if user_input:  # если пользователь ввел хоть что-нибудь (Если не пустая строка, то true)
    if user_input == password:
        print('Welcome')
    else:
        print('Wrong password')
else:
    print('Input password please')  # - Это условие выполнено

# Тернарный оператор
# Когда все выражение проверки if else умещается в одну строку
print('Welcome') if user_input else print('Wrong Password')  # -> Wrong Password

# Синтаксис тернарного оператора:
# [если истина] if [выражение] else [если ложь]
# Пример тернарного оператора:
x, y = 25, 50
big = x if x < y else y
print(big)

# Задача FizzBuzz:
# Числа от 1 – 100
# Если число кратно 3 – Fizz (т.е. делится на три без остатка)
# Если число кратно 5 – Buzz
# Если число кратно 3 и 5 – пишем FizzBuzz
# В остальных случаях просто число


def fizz_buzz(i):
    if 1 <= i <= 100:  # Проверяем, что i находится в диапазоне от 1 до 100
        # Это равнозначно if (i % 3 == 0) and (i % 5 == 0):
        if not (i % 3) and not (i % 5):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
    else:
        print('Число не находится в диапазоне от 1 до 100')


def fizz_buzz_match(i):
    if 1 <= i <= 100:  # Проверяем, что i находится в диапазоне от 1 до 100
        match i:
            # case _ - Это обработка всех остальных случаев, которые не были перехвачены предыдущими case блоками.
            case _ if i % 3 == 0 and i % 5 == 0:
                # Если i делится и на 3, и на 5 без остатка, то выводится 'FizzBuzz'
                print('FizzBuzz')
            case _ if i % 3 == 0:
                # Если i делится на 3 без остатка (но не делится на 5), выводится 'Fizz'
                print('Fizz')
            case _ if i % 5 == 0:
                # Если i делится на 5 без остатка (но не делится на 3), выводится 'Buzz'
                print('Buzz')
            case _:
                # Если ни одно из условий не выполнено, выводится само число i
                print(i)
    else:
        print('Число не находится в диапазоне от 1 до 100')

# Это список list []
numbers_to_test = [1, 2, 3, 5, 7, 15, 150]

for number in numbers_to_test:
    fizz_buzz(number)
for number in numbers_to_test:
    fizz_buzz_match(number)
