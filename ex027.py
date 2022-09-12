#um programa que leia o nome completo de uma pessoa, mostrando
#em seguida o primeiro e o ultimo nome, separadamente
nome = str(input('Digite o nome completo da pessoa: ')).strip()
print('Muito prazer em te conhecer.')
print('Primeiro nome: {}.'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[-1]))
