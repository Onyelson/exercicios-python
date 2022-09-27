'''Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a BASE DE CONVERSÃO:
-1 para binário
-2 para octal
-3 para hexadecimal
'''
print('--=' * 10)
n = int(input('Digite um número inteiro: '))
print('--=' * 10)
print('Escolha para converter: ')
print('1 - Binário \n2 - Octal \n3 - Hexadecimal ')
print('--=' * 10)
escolha = int(input('Digite sua escolha: '))
print('--=' * 10)
if escolha == 1:
    print('A conversão de {} em binário é {}.'.format(n, format(n,'b')))
elif escolha == 2:
    print('A conversão de {} em Octal é {}.'.format(n, format(n, 'o')))
elif escolha == 3:
    print('A conversão de {} em hexadecimal é {}.'.format(n, format(n, 'x')))
else:
    print('Opção invalida. Tente novamente.')
print('--=' * 10)