'''Ex 4. Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com
sua idade, se ele ainda vai se alistar ao serviço militar, se é a hhora de se alistar ou se já passou
do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.'''

x=float(input('Em que ano você nasceu? '))
idade=2022-x
if idade<18:
    print('Ainda não ')
elif idade==18:
    print('Tem que se alistar ')
else:
    i=idade-18
    print('ja paso da época em {} anos '.format(i))
