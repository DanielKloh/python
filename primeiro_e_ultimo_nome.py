'''Ex 10. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e último nome separadamente. Ex.: Janaina Lopes Dias. Primeiro: Janaina Último: Dias.'''

x=input('informe se nome completo: ').split()
p1=x[0]
p2=x[-1]
print('O primeirpo nome é {} e o ultimo nome é {} '.format(p1, p2))