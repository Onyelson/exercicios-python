'''Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com sua idade:
-Se ele ainda vai se alista ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo de alistamento

Seu programa também devera mostrar o tempo que falta ou passou do prazo
'''
from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = ano - nasc
print('Você nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))
if idade < 18:
    print('Você ainda vai se alistar daqui a {} anos.'.format(18 - idade))
elif idade > 18:
    print('Já passou da hora de se alistar tem {} anos.'.format(idade - 18))
else:
    print('É hora de se alistar.')
