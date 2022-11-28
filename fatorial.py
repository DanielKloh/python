'''Ex 4. Crie um programa que solicite o usuário um número N ímpar maior que 1. Em seguida, preencha
uma lista com N números inteiros positivos (suponha que o usuário sempre digitará números inteiros
positivos). Selecione o elemento que está no centro da lista. Ao final, calcule e escreva o fatorial do
elemento selecionado.
'''

n = int(input('Digite um número ímpar, maior que 1: '))

if n<=1 or n%2==0:
    print('Número informado não atende os críterios defindos.')
else:
    l=[]
    for x in range(n):
        num=int(input('Digite um número maior ou igual a zero: '))
        l.append(num)

centro=int(len(l)/2)
elementocentro=l[centro]
fatorial=1

# 1*2*3*4*5=120
for n in range(2, elementocentro+1):
    fatorial*=n
print(f'Lista: {l}')
print(f'O elemento do centro da lista {elementocentro} e seu fatorial é igual {fatorial}')                         