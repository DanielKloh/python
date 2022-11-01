'''Ex 2. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere
que o usuário informou cinco medicamentos distintos). O programa deve informar o nome e o preço do
medicamento mais barato, bem como a média aritmética dos preços informados.
'''

'''nome=input('Digite o nome de um medicamento: ').strip()
prec=float(input('Digite o valor do medicamento: '))

nom=nome
valor=prec
soma=valor

for c in range(1,5):
    nome=input('Digite o nome de um medicamento: ').strip()
    prec=float(input('Digite o valor do medicamento: '))
    soma+=prec

    if prec<valor:
        nom=nome
        valor=prec
        

media=(soma)/5
        
print('O medicamento mais barato é {} e a media aritimetica é {}'.format(nome, media))'''

soma=0

medicamento=input('Medicamentos:')
preco=float(input('preço: '))

maisbarato=medicamento
menorpreco=preco

somapreco=preco

for x in range(4):
    medicamento=input('medicamento ')
    preco=float(input('R$ '))
    if preco<menorpreco:
        menorpreco=preco
        maisbarato=medicamento
    soma+=preco
media=soma/5

print('{} é o medicamento mais barato e custa R$ {} \n Media de preços: {}'.format(maisbarato,menorpreco,media))