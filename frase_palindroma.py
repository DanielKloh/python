'''Ex 2. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços'''

frase=input('Digite uma frase: ').strip().upper()#  Apos a sopa

palavras=frase.split()#  apos a sopa
junto=''.join(palavras)# Aposasopa
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]

if inverso==junto:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')