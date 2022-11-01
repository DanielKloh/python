#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''Ex 3. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.'''
from math import cos, radians
from math import sin
from math import tan
x=float(input('Digite um angulo  qualquer '))
c=cos(radians(x))
s=sin(radians(x))
t=tan(radians(x))
print('O seno desse número é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f} '.format(s,c,t))
