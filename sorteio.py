'''Ex 4. Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

from random import randint
x1=input('Qual o nome do aluno?')
x2=input('Qual o nome do aluno?')
x3=input('Qual o nome do aluno?')
x4=input('Qual o nome do aluno?')

x=randint(1,4)
if x==1:
    print('{} vai apagar o quadro '.formart(x1))
if x==2:
    print('{} vai apagar o quadro '.format(x2))
if x==3:
    print('{} vai apagar o quadro '.format(x3))
if x==4:
    print('{} vai apagar o quadro '.format(x4))
#   OU:
#
#   from random import choice
#   x1=input('Qual o nome do aluno?')
#   x2=input('Qual o nome do aluno?')
#   x3=input('Qual o nome do aluno?')
#   x4=input('Qual o nome do aluno?')
#   lista = [x1, x2, x3, x4]
#   scolhodo = choice(lista)
#   print('O aluno escilhido foi {}'.format(scolhodo))