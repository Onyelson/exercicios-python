'''Faça um programa que leia três números e mostre qual é o maior e qual
o menor'''
n1 = input('Primeiro número: ')
n2 = input('Segundo número: ')
n3 = input('Terceiro número: ')
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é: \033[33m{}\033[m'.format(maior))
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor =n3
print('O menor número é: \033[31m{}\033[m'.format(menor))
'''primeiro entender a lógica depois procurar um meio mais facil que seria a lista
lista = [n1, n2, n3]
print('O maior número é: {}'.format(max(lista)))
print('O menor número é: {}'.format(min(lista)))'''