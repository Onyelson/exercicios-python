#um prog que peça o km rodado de um caro alugado
#quantidade de dias alugados, calcular o preço a pagar
#sabendo que o carro custa R$60 por dia e R$0.15 por km rodado
km = float(input('Quanto percorreu o carro alugado em Km: '))
dia = int(input('Por quantos dias o carro foi alugado: '))
pago = (dia * 60) + (km* 0.15)
print('O valor a pagar é R${}'.format(pago))