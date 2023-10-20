# Это обычная функция генерирует последовательность в
# обратном порядке
def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result

print(countdown(4)) # -> [3, 2, 1, 0]

# Это функция генератор делает тоже самое
def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1
g = gen_countdown(4)
print(next(g))

for i in gen_countdown(4):
    print(i)
