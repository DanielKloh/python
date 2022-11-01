'''Ex 5. Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

soma=0
par=0
impar=0

from random import randint
x=randint(1,2)
if x%2==True:
    x=par
else:
    x=impar
while True:
    x=int(input('Escola impar(1) ou par(2)'))
    if x==2:
        print('Ganhou')
        soma+=1
    else:
        x==1
        print('Perdeu')
        break

print('Ganhou {} veses'.format(soma))