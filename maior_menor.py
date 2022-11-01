'''Ex 2. Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.'''

x=float(input('Digite o primeir número '))
x2=float(input('Digite o segundo número '))
x3=float(input('Digite o terceiro número '))
maior=x
if x>x2 and x>x3:
    print('{} esse é o maior '.format(x))
if x2>x and x2>x3:
    print('{} esse é o maior '.format(x2))
menor=x
if x3>x and x2>x:
    print('{} esse é o menor '.format(x))
if x2>x and x2>x3:
    print('{} esse é o meno '.format(x))