'''Ex 6. Criei um programa que faça o computador jogar Jokenpô com você'''

from random import randint
x=int(input(' 1:tesoura \n 2:pedra \n 3:papel\n   '))
r=randint(1,3)
if r==1:
    if x==1:
        print('empate')
    elif x==2:
        print('Ganhou!!')
    elif x==3:
        print('PERDEU')
elif r==2:
    if x==1:
        print('perdeu')
    elif x==2:
        print('empate')
    elif x==3:
        print('ganhou')
elif r==3:
    if x==1:
        print('ganho')
    elif x==2:
        print('perdeu')
    elif x==3:
        print('empate')