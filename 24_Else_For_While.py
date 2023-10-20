for i in range(5):
    print(i)

print('The End')

for i in range(5):
    if i == 6:
        print(i)
        break
else:
    print('The End')

# Аналог инструкции else
flag = False
for i in range(5):
    if i == 4:
        flag = True
        break
if flag:
    print('Four was found')