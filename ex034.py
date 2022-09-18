'''Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento
de 10%. Para inferiores ou iguais um aumento de 15%'''
salario = float(input('Digite o valor do salário a passar por reajuste: R$'))
aumento10 = salario + salario * 0.1
aumento15 = salario + salario * 0.15
if salario > 1250:
    print('Com o salário de R${:.2f} o aumento será de 10%, reajuste para: R$\033[32m{:.2f}\033[m.'.format(salario, aumento10))
else:
    print('Com o salário de R${:.2f} o aumento será de 15%, reajuste para: R$\033[32m{:.2f}\033[m'.format(salario, aumento15))

