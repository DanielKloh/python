'''Ex 1. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

x=int(input('Digite um numero inteiro: '))
tot=0

for c in range(1,x+1):
    if x%c==0:
        print('\033[33m' , end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO numero {x} foi divisivel {tot} veses')

if tot==2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')