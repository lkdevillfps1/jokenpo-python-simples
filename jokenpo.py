from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é a sua escolha? '))
print('\n', '----------------'.center(50))
print('\033[31mJO\033[m'.center(50)) #COLORAÇÃO NO PYTHON 30-39
sleep(0.5)
print('\033[32mKEN\033[m'.center(60))
sleep(0.5)
print('\033[33mPO!!\033[m'.center(70))
print('  ----------------'.center(50))
print(f'O Computador jogou {itens[computador]}')
print(f'O Jogador jogou {itens[jogador]}')
print('-=' * 20)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador venceu! ')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('JOGADA INVALIDA!' )
elif computador == 1: #computador jogou papel
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador venceu! ')
    elif jogador == 0:
        print('Computador venceu')
    else:
        print('JOGADADA INVALIDA!')

elif computador == 2: #computador jogou tesoura
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    else:
        print('JOGADA INVALIDA!')















