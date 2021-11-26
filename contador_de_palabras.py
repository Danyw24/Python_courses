def run ():
    palabra = input('Ingrese palabra:')
    palabras = 1
    for p in palabra:
        if p == ' ':
            palabras += 1
        else:
            pass
    print(palabras)

if __name__ == '__main__':
    run()
    #Nota 4.3/5