def polindrom():
    a = input('Введите слово')
    b = a[::-1]
    if a == b:
        print('Это слово полиндром: ', a, b)

    else:
        print('Это слово не полиндром: ', a, b)
pol  = polindrom()
print(pol)