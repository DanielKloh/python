'''Ex 5. O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

x1=input('Qual o nome do aluno?')
x2=input('Qual o nome do aluno?')
x3=input('Qual o nome do aluno?')
x4=input('Qual o nome do aluno?')

lista=[x1,x2,x3,x4]
shuffle(lista)
print('Os alunos vão apresentar nessa ordem {}'.format(lista))