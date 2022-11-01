#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''Ex 2. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''
from math import hypot
x=float(input('Cateto oposto '))

y=float(input('Cateto adjacente '))

hip=hypot(x,y)
print('O valor da hipotenusa é {:.2f} '.format(hip))
