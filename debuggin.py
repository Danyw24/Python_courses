def divisors (num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1: # err
            divisors.append(i)
    return divisors

def run ():
    num = int(input(' numero >>'))
    print(divisors(num))
    print('Fin')

if __name__ == '__main__':
    run()