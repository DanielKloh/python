'''Ex 1. Construa um programa para fazer uma pequena entrevista com os alunos de uma turma. Na
entrevista, são informados o sexo e a idade de cada aluno. Considere que o usuário não sabe quantos
alunos existem na turma. O programa deve exibir a quantidade de homens acima de 18 anos e a
quantidade de mulheres de qualquer idade. Para encerrar o programa, o usuário deve informar uma idade
negativa.'''

soma=0
whomen=0
idade=1

while idade>0:
    idade=int(input('Digite a sua idade: '))
    sexo=(input('Digite o seu sexo[M/F]: ')).strip().upper()
    

    if sexo=='M' and idade>=18:
        soma+=1
    elif sexo=='F':
        whomen+=1
    elif idade <0:
        break
        
print('{} homens com mais de 18 anos e {} mulheres '.format(soma,whomen))