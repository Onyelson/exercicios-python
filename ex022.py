'''Crie um programa que leia o nome completo de uma pessoa e mostre
O nome com todas as letras maiúsculas, minúsculas, quantas letras
sem considerar espaços, quantas letras tem o primeiro nome'''
nome = str(input('Informe o nome: ')).strip()
print('Tudo maiúsculo: {}.'.format(nome.upper()))
print('Tudo minúsculo: {}'.format(nome.lower()))
print('Número de letras que o nome completo possui: {}.'.format(len(nome) - nome.count(' ')))
n = nome.split(' ')[0]
print('O número de letras no primeiro nome que é {}: {}.'.format(nome.split()[0], len(n)))

#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
