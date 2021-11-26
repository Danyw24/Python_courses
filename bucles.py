def run ():
    LIMITE = 1000
    contador = 0
    while contador <= 1000:
        print('la potencia de 2 por ' + str(contador) + ' es: ' + str(2**contador))
        contador = contador + 1

if __name__ == '__main__':
    run()
