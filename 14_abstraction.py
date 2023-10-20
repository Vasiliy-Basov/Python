# Расчет массы ингридиентов
def get_salt_mass(m):
    return m * 15 / 1000


def get_pepper_mass(m):
    return m * 5 / 1000

print(get_pepper_mass(1500))
print(get_salt_mass(1500))

# другой способ
ingredients = dict(salt=15,
                   pepper=5)

def get_ingredient_mass(m, ingr):
    return m * ingredients.get(ingr, 0) / 1000

print(get_ingredient_mass(1500, 'salt'))

print(help(print))

def print_wrapper(text):
    with open('readme', 'a', encoding='utf-8') as f:
        print(text, file=f)
print_wrapper('тест')