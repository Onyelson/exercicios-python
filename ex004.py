#testar tipos e se é 'x' ou não
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('É alpha númerico? ', a.isalnum())
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('Só está em maiúsculo? ', a.isupper())
print('Só está em minúsculo? ', a.islower())
print('É alfabético? ', a.isalpha())
print('Está capitalizada? ', a.istitle())
