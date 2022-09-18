'''Desenvolvar um programa que leia o comprimento de três restas e diga ao
usuário se elas podem ou não formar um triângulo'''
l1 = float(input('Digite o valor da primeira reta: '))
l2 = float(input('Digite o valor da segunda reta: '))
l3 = float(input('Digite o valor da terceira reta: '))
if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l1+l2):
    print('com os valores das retas sendo \033[31m{}\033[m, \033[34m{}\033[m e \033[33m{}\033[m pode sim se formar um triângulo'.format(l1, l2, l3))
else:
    print('Não se pode formar um triângulo')
