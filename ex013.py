#ler um valor de salario e mostrar o mesmo com aumento de 15%
s = float(input('Digite o valor do salário: '))
a = s * (15 / 100)
sn = s + a
print('O seu novo salário reajustado em 15% é de R${:.2f}'.format(sn))