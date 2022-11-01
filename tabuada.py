'''Ex 4. Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.'''

n=int(input('Digite um número que queira saber a sua tabuada: '))
print('tabuada do {}'.format(n))

for c in range(1,11):
    taboada=c*n
    print(' {} X {} = {}'.format(n,c,taboada))