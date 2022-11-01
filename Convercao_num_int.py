'''Ex 2. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: a) para binário; b) octal e c)hexadecimal. Dica: para as três bases
solicitadas existem funções no Python.'''

x=int(input('Digite um número inteiro: '))
num=float(input('programa de converção##\n 1: Para binario \n 2: Octal \n 3: hexadecimal \n  :  '))
if num>3 or num<0:
    print('Opção invalida!!')
if num==1:
    bi=bin(x)
    print('Binario vale {} '.format(bi))
if num==2:
    oc=oct(x)
    print('Octal vale {}'.format(oc))
if num==3:
    h=hex(x)
    print('Hexadecimal vale {}'.format(h))