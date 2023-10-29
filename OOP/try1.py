a = False
while a == 0:
    try:
        a, b = map(int, input('введите целое число:').split())
    except ValueError:
        print('нужно ввести целое число, попробуйте снова')
    else:
        a = True
    
