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
        comandos.append(list(Comandos)[random.randint(0, 1)])
    return comandos



def trem(comm):
    position_end = 0

    for position in comm:
        position_end += position.value
        print(position)

    print(position_end)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    COMMANDS = gera_comandos()
    trem(COMMANDS)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
