# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
from enum import Enum

class Comandos(Enum):
    ESQUERDA = -1
    DIREITA = 1

def gera_comandos():
    size = random.randint(1, 30)
    comandos = []
    for x in range(size):
        ## comandos.append(list(Comandos)[random.randint(0, 1)])
        comandos.append(list(Comandos)[0])

    return comandos



def trem(comm, interval):
    position_end = 0

    for position in comm:
        print('current position:', position_end, 'command: ', position)

        if position_end + position.value < interval.get('min') or position_end + position.value > interval.get('max'):
            continue

        position_end += position.value

    print('position end: ', position_end)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    interval = { 'max': 10, 'min': -2 }

    COMMANDS = gera_comandos()
    trem(COMMANDS, interval)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
