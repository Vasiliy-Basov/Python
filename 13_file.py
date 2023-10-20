file = open('readme.txt', 'w', encoding='utf-8')
file.write('абвdfg')
file.close()
file = open('readme.txt', encoding='utf-8')
data = file.read()
print(data)

pic = 'p.jpg'
file = open(pic, 'rb')
new_file = open('copy_' + pic, 'wb')
new_file.write(file.read())

with open('readme.txt', 'w', encoding='utf-8') as file:
    file.write('hello world \n')
with open('readme.txt', 'a', encoding='utf-8') as file:
    file.write('new line \n')
with open('readme.txt', 'a', encoding='utf-8') as file:
    file.writelines('new line1')
with open('readme.txt', 'r', encoding='utf-8') as file:
    print(file.read())