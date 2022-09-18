"""style       text            background
0 none      30 branco       40 a 47 mesma cores
1 bold      31 vermelho
4 underline 32 verde
7 negative  33 amarelo
            34 azul
            35 roxo
            36 azul celeste
            37 cinza
\033[0;33;44m #[ style;text;background m"""
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Onyelson'
print('Olá! Muito prazer em te conhecer {}{}{}.'.format('\033[4;34m', nome, '\033[m'))

nome2 = 'Onyelson'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! muito prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome2, cores['limpa']))