def main():
    d = {'website': 'google'}
    try:
        print(фыва)
        data = d['url']
    except KeyError:
        data = 'http://'
        print(data)
    except Exception as ex:
        print(ex)
        print('oops')
    finally:
        print('Very important action')
main()

def main():
    d = {'website': 'google'}
    try:
        print(фыва)
        data = d['url']
    except:
        data = 'http://'
        print('inside except', data)
        return data
    finally:
        print('Very important action')
result = main()
print(result)


def main():
    d = {'website': 'google', 'url': 'google.ru'}
    try:
        data = d['url']
    except:
        data = 'http://'
    else:
        data = data.upper()
    print(data)
main()