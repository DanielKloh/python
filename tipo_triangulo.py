'''Ex 2. Refaça o Exercício 4 da Aula 7, acrescentando o recurso de mostrar que tipo de triângulo será
formado: a) Equilátero: todos os lados são iguais; b) Isósceles: dois lados iguais; c) Escaleno: todos os
lados diferentes.'''

x1=float(input('Inforne o comprimento da primeira reta: '))
x2=float(input('Inforne o comprimento segunda reta: '))
x3=float(input('Inforne o comprimento terceira reta: '))
if x1<x2+x3 and x2<x1+x3 and x3<x2+x1:
    print('É possivel formar um triangulo ')
    if x1==x2 and x1==x3 and x2==x3:
        print('Triangulo equilatero')
    elif x1!=x2 and x1!=x3 and x3!=x2:
        print('Triangulo escaleno')            
    else:
        print('Triangulo isocelis')        
else:
    print('não podem formar um triangulo ')