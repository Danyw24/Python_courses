def run():
    respuesta = input('Introzuca acronimo: ')
    acronimo = ''
    for p in respuesta:
        if p == p.upper():
            acronimo += p
        else:
            pass
    print(acronimo)

if __name__ == '__main__':
    run()

    #Nota 4.7/5