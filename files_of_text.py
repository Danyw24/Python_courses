# def read ():
#     numbers = []
#     with open('./names.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             numbers.append(line)
#     print(numbers)


# def write ():
#     names = ['pablo','miguel','cristian','facundo']
#     with open('./prueba/namess.txt', 'w', encoding='utf-8') as w:
#         for name in names:
#             w.write(name)
#             w.write('\n')


# def run():
#     write


# if __name__ == '__main__':
#     run() 
    

#NO ACTIVAR, 1.3GB POR EJECUTO
# def run():
#     names = []
#     for i in range(0,99999999):
#         names.append('1',)
#     destination = './prueba/'
#     for i in range(0, 5):
#         with open(destination + '.txt', 'w', encoding='utf-8') as f:
#             for name in names: 
#                 f.write(name)
#                 f.write('/n')
#         destination = destination + 'owo'

# if __name__ == '__main__':
#     run() 


names = ['Pablo','Rodrigo']



def read ():
    with open('names.txt', 'r', encoding='utf-8') as f:
        for name in f:
            print(name)


def write ():
    with open('names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)


def append():
    with open('names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)


def delete ():
    with open('names.txt', 'w', encoding='utf-8') as f:
        f.write('')


def run():
    delete()


if __name__ == '__main__':
    run()














