from time import sleep

def pi(time:float = 0):
    '''число пи, аргументом является время на полное заполение одной строки длиной 64 символа(устанавливать слишком низкие значения не рекомендуется)'''
    tick = 0
    line = []

    #ost и second это числа, которые при делении равны числу пи
    ost = 355
    second = 113
    while True:
        tick += 1
        if ost < second:
            ost *= 10

        new = ost // second
        ost -= new * second

        #Так как длина строки 64 символа, то делим время на каждый символ
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
