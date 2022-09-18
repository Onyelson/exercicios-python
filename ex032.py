'''Faça um programa quie leia o ano qualquer e mostre se ele é
BISSEXTO'''
from calendar import isleap
from datetime import date
ano = int(input('Digite o ano a ser consultado se é bissexto ou digite 0 pra ver se o ano atual é bissexto: '))
if ano == 0:
    ano = date.today().year
if isleap(ano): #if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {}{}{} é SIM bissexto.'.format('\033[34m', ano, '\033[m'))
else:
    print('O ano {}{}{} NÃO é bissexto.'.format('\033[31m', ano, '\033[m'))