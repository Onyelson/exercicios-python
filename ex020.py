#o mesmo professor quer sortear a ordem de apresentação
#de trabalho dos alunos. faça um programa que leia o nome dos 4
#alunos e mostre a ordem sorteada
from random import  shuffle
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('ALuno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A Ordem de apresentação será ')
print(lista)
