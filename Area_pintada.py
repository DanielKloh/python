'''Ex 2. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma
área de 2m².'''

h=float(input('Informe o tamanho da altura de uma parede:'))
b=float(input('Iforme o tamanho da largura de uma parede: '))
A=b*h
tinta=A/2
print('Serão necessarias {} latas de tinta para pintar essa parede '.format(tinta))
