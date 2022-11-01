'''Ex 2. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maior=0
menor=0
for c in range(5):
    peso=float(input('Digite o peso de uma pessoa: '))
    if c==1:
        maior=peso
        menor=peso
    else:
        if maior<peso:
            maior=peso
        elif menor>peso:
            menor=peso
print('{} é o mais pesado e {} é o menos pesado'.format(maior,menor))