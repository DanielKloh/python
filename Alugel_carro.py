'''Ex 3. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.'''

km=float(input('Qantos km foram percorridos? '))
dia=float(input('Quantos dias ficou alugado? '))
f=(km*60)+(dia*0.15)
print('O valor a se pagar pelo carro é de R${} '.format(f))
