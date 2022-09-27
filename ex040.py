"""Crie um programa que leia duas notas de um aluno, calcule a sua média
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('com média {:.1f} você está REPROVADO'.format(media))
elif (media >= 5) and (media <= 6.9):
    print('Com média {:.1f} você está de RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Com média {:.1f} você está APROVADO'.format(media))