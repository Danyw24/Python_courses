def run ():
    for number in range(1000):
        if number / 2 != 0:
            continue
        print(str(number))            


if __name__ == '__main__':
    run()