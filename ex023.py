#faça um programa que leia um número de 0 a 9999 e mostre
#na tela cada um dos dígitos separados. Ex: digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
n = int(input('Digite um número de 0 a 9999: '))
u = (n // 1) % 10
print('O digito da unidade é: ', u)
d = (n // 10) % 10
print('O dígito das dezenas é: ', d)
c = (n // 100) % 10
print('O digito das centenas é: ', c)
m = (n // 1000) % 10
print('O digito do milhar é: ', m)
