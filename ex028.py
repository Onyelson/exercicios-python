'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero
escolhido pelo computador. O programa devera escrever na tela se o usuário
venceu ou não.'''

from random import randint
from time import sleep
comp = randint(0, 5)
player = int(input('Tente acerta o número que o computador pensou, escolha um valor entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if player == comp :
    print('Você acertou, parabéns!')
else:
    print('Você errou, eu pensei no número {}{}{} e não no {}{}{}, obrigado.'.format('\033[34m', comp, '\033[m', '\033[31m', player, '\033[m'))


