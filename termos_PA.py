'''Ex 4. Refaça o Ex 6 da Aula 13, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.'''

primeiro=int(input('Primeiro termo: '))
razao=int(input('razãp da PA: '))
termo=primeiro
cont=1
while cont<=10:
    print(f'{termo}', end=' ')
    termo+=razao
    cont+=1
print('Fim')
