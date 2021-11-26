def run():
    print('Por favor rellene los datos pedidos')
    nombre = input('Nombre: ')
    fhna = input('Fecha de nacimiento (en palabras): ') #fecha de nacimiento
    direccion = input('Dirección: ')
    metas = input('Metas personales: ')

    if len(nombre) > 1 and len(fhna) > 1 and len(direccion) > 1 and len(metas) > 1:
        print(f'''
        Nombre: {nombre}
        Fecha de nacimiento: {fhna}
        Dirección: {direccion}
        Metas: {metas}
        ''')
    else:
        print('Datos incorrectos, introduzca datos validos y de mas de un digito')

if __name__ == '__main__':
    run()

    #Nota 4.0 porque funciona y no se busco en google pero puede ser expuesta a errores