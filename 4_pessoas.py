'''Ex 3. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 1) a
média de idade do grupo. 2) qual é o nome do homem mais velho. 3) quantas mulheres têm menos de 20 anos.'''

somaidade=0
maioridadehomem=0
homemmaidvelho=0
mulheridade=0
mulhermenor=0
mediaidade=0
for p in range(1,5):
    nome=(input('Digite o seu nome: ')).strip()
    idade=int(input('Digite a sua idade'))
    sexo=(input('Digite o genero[M/F]')).strip().upper ()

    somaidade+=idade
    if p==1 and sexo in 'M':
        maioridadehomem=idade
        homemmaidvelho=nome

    if sexo in 'M' and idade>maioridadehomem:
        maioridadehomem=idade
        homemmaidvelho=nome

    if sexo in 'F' and idade <20:
        mulheridade+=1

mediaidade=somaidade/4

print('A média da idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem,homemmaidvelho))
print('{} tem mais de 20 anos'.format(mulhermenor))