'''Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO
do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ele não pode exceder
30% do salário ou então o empréstimo será negado.
'''
from time import sleep
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))
tempo = anos * 12 #simples, transformar anos em meses
parcela = casa / tempo
print('O emprestimo não será aprovado se o valor da prestação ultrapassar \033[31m30%\033[m do seu salário.')
print('PROCESSANDO...')
sleep(3)
if parcela < salario * (30/100):
    print('A prestação será de \033[32mR${:.2f}\033[m, \033[32mEMPRESTIMO APROVADO\033[m.'.format(parcela))
else:
    print('A prestação no valor de \033[32mR${:.2f}\033[m ultrapassou o seu limite de \033[31m30%\033[m do salário, \033[31mEMPRESTIMO NEGADO\033[m.'.format(parcela))