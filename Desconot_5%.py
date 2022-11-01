'''Ex 1. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de
desconto.'''

x=float(input('Informe o preço atual do produto: '))
d=((x*0.05)-x)*-1
print('O novo preço desse produto com 5% é {} '.format(d))
