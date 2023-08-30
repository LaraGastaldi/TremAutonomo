# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
from enum import Enum

class Comandos(Enum):
    ESQUERDA = -1
    DIREITA = 1


def trem(comm, interval, position_end):
    for position in comm:
        print('current position:', position_end, 'command: ', position)
        if position_end + position.value < interval.get('min') or position_end + position.value > interval.get('max'):
            continue

        position_end += position.value

    print(position_end)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('Informe o número mínimo dos trilhos: ')
    min_pos = int(input())

    print('Informe o número máximo dos trilhos: ')
    max_pos = int(input())

    print('Informe a posição atual do trem: ')
    current_pos = int(input())

    comandos = []

    for x in range(30):
        print('Informe o comando (E para esquerda, D para direita, em branco para sair): ')
        current_command = input().lower()

        if current_command != 'e' and current_command != 'd':
            break

        if current_command == 'e':
            comandos.append(Comandos.ESQUERDA)
        else:
            comandos.append(Comandos.DIREITA)

    trem(comandos, {'max': max_pos, 'min': min_pos}, current_pos)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
