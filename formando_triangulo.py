'''Ex 4. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo.'''

x1=float(input('Inforne o comprimento da primeira reta: '))
x2=float(input('Inforne o comprimento segunda reta: '))
x3=float(input('Inforne o comprimento terceira reta: '))
if x1<x2+x3 and x2<x1+x3 and x3<x2+x1:
    print('não podem formar um triangulo ')
else:
    print('É possivel formar um triangulo ')