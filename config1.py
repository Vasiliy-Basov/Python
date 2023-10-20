

token = 'from_config'
email = 'google@google.ru'

def main():
    print('__name__ variable of the '
          'config1.py module \n', __name__)

# т.е. идет проверка если переменная __name__ принимает
# значение __main__ т.е. файл запускается как главный и
# идет выполнение главной функции main()
if __name__ == '__main__':
    main()