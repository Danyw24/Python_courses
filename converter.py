
def converterMoney (valOfMoney, Money, NameOfMoney):
    floatMoney = float(Money)
    finalMoney = round( floatMoney / valOfMoney , 2)
    print('Tienes $' + str(finalMoney) + ' ' + NameOfMoney )

# Starting 
def startMoneyConverter () :
    print('''   
    Bienvenido a el conversor de monedas de danyw24 
    v1.1

    (1). Dolares
    (2). Soles
    (3). Pesos Mexicanos
    ''')
    selectedOptionMoney = input('Escoja una opcion >>')

    if selectedOptionMoney == '1' :

        M = input(''' 
        De Pesos colombianos a Dolares Estadounidenses

        Cuanto dinero Tienes?
    
        >>    ''')
        converterMoney(3860, M, 'Dolares')

    elif selectedOptionMoney == '2' :
        M = input(''' 
        De Pesos colombianos a Soles Peruanos

        Cuanto dinero Tienes?
    
        >>    ''')
        converterMoney(931, M, 'Soles')

    elif selectedOptionMoney == '3' :
         M = input(''' 
          De Pesos colombianos a Pesos Mexicanos
          Cuanto dinero Tienes?
  
         >>    ''')
         converterMoney(191, M, 'Pesos')
    else: 
        print('"' + str(selectedOptionMoney) + '"' + ' No es una opcion valida ')

startMoneyConverter();

