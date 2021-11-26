def run():
    palabra = '''
    El elefante es ________ y tambien _________,
    El puma es ________,
    El sol ________ muy fuerte cuando lo miras
    '''
    palabras = ['grande','pesado','rapido','brilla']
    puntos = 0
    print(palabra)
    for p in palabras:
        respuesta = input('palabra: ')
        if respuesta == p:
            print('Correcto: ' + p)
            puntos += 1
        else:
            print('Mal')
            pass
    print(f'Tus puntos son {puntos}/4')


if __name__ == '__main__':
    run()

    #Nota 4.7/5