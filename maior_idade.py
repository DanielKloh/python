'''Ex 1. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.'''

soma=0
soma2=0

for c in range(7):
    nasc=float(input('Informe a data de nascimento: '))
    
    idade=2022-nasc
    if idade>=18:
        soma+=1
    if idade<18:
        soma2+=1
print('{} atiniram a mior idade, e {} não atingiram a maior idade'.format(soma,soma2))