'''Ex 1. Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

x=int(input('Informe um ano que desejas analisar: '))
if x%4 == 0:
    print('Esse ano é bissexto! ')
else:
    print('Esse ano não é bissexto! ')