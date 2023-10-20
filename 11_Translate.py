trans = 'Видео про файловые объекты, про чтение и запись в текстовые и бинарные файлы, о типах ввода-вывода (IO) в языке Python и закончим контекстным менеджером w'


def match(text):
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return not alphabet.isdisjoint(text.lower())


def tr(text):
    final = []
    rus = dict(а='a', б='b', в='v', г='g', д='d', е='e', ё='yo', ж='zh', з='z', и='i', й='j', к='k', л='l', м='m',
               н='n', о='o', п='p', р='r', с='s', т='t', у='u', ф='f', х='h', ц='c', ч='ch', ш='sh', щ='shch', ъ='"',
               ы='y', ь='\'', э='e', ю='yu', я='ya')

    for letter in text:
        if letter.istitle() and match(letter):
            final.append(rus.get(letter.lower()).title())
        elif match(letter):
            final.append(rus.get(letter))
        else:
            final.append(letter)
    return ''.join(final)


print(tr(trans))
