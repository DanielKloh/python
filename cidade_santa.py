'''Ex 1. Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “Santa”.'''

cidade=input('Escreva o nome de uma cidade: ').lower()
x=cidade.find('santa')
if x==cidade.find('santa'):
    print('Essa cidade começa com o nome santa')
else:
    print('Essa cidade não começa com o nome santa')