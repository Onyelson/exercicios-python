#um programa que leia o comprimento do cateto oposto e
#do cateto adjacente de um triângulo retângulo, calcule e mostre a
#Dona Hipotenusa

from math import hypot
catOp = float(input('Informe o cateto oposto: '))
catAd = float(input('Informe o cateto adjacente: '))
hipo = hypot(catOp, catAd)
print('Com os valores dos catetos {} e {} sua hipotenusa vale {:.2f}'.format(catOp, catAd, hipo))
