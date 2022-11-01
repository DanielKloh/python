'''Ex 4. Para construir o programa a seguir, considere que os usuários só informarão números inteiros positivos.
Crie um programa que receba 5 números digitados e, ao fim, exibir quantos números são pares.'''

pares=0
for cont in range(5):
    num=int(input('digite um número: '))
    if num%2==0:
        pares+=1
print('Quantidade de números pares digitados: {}'.format(pares))