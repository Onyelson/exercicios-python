#calcular área e volume de tinta considerar 1 litro para 2m**2
l = float(input('Qual a largura da parede(m): '))
a = float(input('Qual a altura da parede(m): '))
ar = l * a
lt = ar / 2
print('Em uma área de {}m2 serão necessários {}l de tinta.'.format(ar, lt))
