'''Desenvolva um programa que pergunte a distancia de uma viagem em Km
Calcule o preço da passagem, cobrando R$o,50 por Km para viagens de até
200km e R$0,45 para viagens mais longas'''
dis = int(input('Qual a distancia da viagem em Km? '))
'''if dis <= 200: #minha primeira solução e depois uma mais pequena feita pelo guanabara
    print('Com a distancia sendo {}Km o valor por Km é de R${:.2f}, seu total a pagar será R${:.2f}.'.format(dis, 0.50, dis*0.50))
else:
    print('Com a distancia sendo {}Km o valor por Km é de R${:.2f}, seu total a pagar será R${:.2f}.'.format(dis, 0.45, dis*0.45))'''
print('Você está preste a começar uma viagem de \033[33m{}\033[mkm'.format(dis))
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print('E o preço da sua passagem será de R$\033[32m{:.2f}\033[m'.format(preço))