'''Ex 3. Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma
das mensagens: a) O primeiro valor é maior. b) O segundo valor é maior. c) Não existe valor
maior'''

x1=int(input('Informe o primeiro valor: '))
x2=int(input('Informe o segundo valor: '))
if x1>x2:
    print('O primeiro  valor é o maior. ')
else:
    print('O segundo valor é o maior. ')
if x1==x2:
    print('Não existe valor maior! ')
