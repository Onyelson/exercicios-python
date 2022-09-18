'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.'''
v = int(input('Qual a velocidade do carro em Km/h? '))
limite = 80
multa = (v - limite) * 7
if v > limite:
    print('Você foi multado em R$\033[32m{:.2f}\033[m por está acima do limite de velocidade.'.format(multa))
else:
    print('Você está dentro do limite de velocidade, tenha um bom dia.')