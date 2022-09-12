#um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez
#em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('Ela aparece a primeira vez na posicão {}.'.format(frase.find('A')+1))
print('E pela última vez na posição {}.'.format(frase.rfind('A')+1))