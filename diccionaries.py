# methods .values() , .item() , .key()

Daniel = {
    'age' : 23,
    'contry' : 'Colombia',
    'job' : 'programer',
    'money' :  4000000,
}

for key , value  in Daniel.items():
    print(key + ' : ' + str(value))