'''Escreva um programa que leia 2 NÚMEROS INTEIROS e compare-os
mostrando na tela a mensagem:
-O primeiro valor é maior
-O segundo valor é menor
-Não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior e o segundo é menor.')
elif n1 < n2:
    print('O segundo valor é maior e o primeiro é menor')
else:
    print('Não existe valor maior, os dois são iguais')