# Le um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

'''Ex 1. Cria um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua
porção inteira.'''
from math import trunc
n=float(input('Digite um número real qualquer '))
x=trunc(n)
print('A porção imnteira desse número é {} '.format(x))