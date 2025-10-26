from time import sleep

def pi(time:float = 0):
    '''число пи, аргумент это кол-во чисел после запятой(устанавливать слишком высокие значения не рекомендуется)'''
    tick = 0
    line = []
    ost = 355
    second = 113
    while True:
        tick += 1
        if ost < second:
            ost *= 10

        new = ost // second
        ost -= new * second

        sleep(time/64)
        line.append(new)
        if len(line) == 64:
            print()
            line = []

        print(new, end='')
        if tick == 1:
            print('.', end='')

time = float(input('enter the time difference(seconds): '))
pi(time)