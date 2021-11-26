def run ():
    num = int(input('Ingrese un numero positivo >>'))
    assert num > 1, 'Ingrese un numero positivo (1) y no negativo (-1)'
    print(num)


if __name__ == '__main__':
    run()