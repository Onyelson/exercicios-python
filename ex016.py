#Um programa que leia um número Real qualquer
#pelo teclado e mostre na tela sua porção interia.
#ex Digite um numero:7.954
#o numero 7.954 tem a parte inteira 7.
'''from math import trunc
num = float(input('Digite um número com casas decimais: '))
print('Sua porção inteira é {}'.format(trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitador foi {} e a sua parte inteira é {}'.format(num, int(num)))

