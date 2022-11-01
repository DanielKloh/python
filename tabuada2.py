'''Ex 4. Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

tab=int(input('Digite um número q deseja saber a taboada: '))
for c in range(1,11):
            total=tab*c
            print(f'{tab} x {c} = {tab * c}')

while True:
    tab=int(input('Digite um número q deseja saber a taboada: '))
    if tab>0:
        for c in range(1,11):
            total=tab*c
            print(f'{tab} x {c} = {tab * c}')
    else:
        break
print('Cabô')
