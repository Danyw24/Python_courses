def run ():
    import math
    square_root = { i : round(math.sqrt(i),2) for i in range(0,1001)}
    print(square_root)


if __name__ == '__main__':
    run() 