#ler valor e mostra o mesmo com 5% de desconto
valor = float(input('Digite o valor do produto a ser descontado 5%: '))
des = valor * (5 / 100)
nvalor = valor - des
print('O novo valor é R${:.2f}.'.format(nvalor))