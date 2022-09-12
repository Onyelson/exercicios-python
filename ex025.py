#Um programa para verificar se o nome de uma pessoa tem SILVA no nome
nome = str(input('Digite o nome: ')).strip()
print('O nome tem Silva? {}'.format('silva' in nome.lower()))