'''Crie um programa que leia um número inteiro e mostre na tela se é
PAR ou IMPAR'''
n = int(input('Digite um número: '))
'''if n % 2 == 0:
    print('O número é PAR!')
else:
    print('O número é IMPAR!')'''
print('O número \033[34m{}\033[m é PAR'.format(n) if n % 2 == 0 else 'O número \033[36m{}\033[m é IMPAR'.format(n))