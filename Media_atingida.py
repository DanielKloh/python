'''Ex 5. Crie um programa que leia duas notas de um aluno mostrando uma mensagem no final, de
acordo com a média atingida: a) média abaixo de 5.0: REPROVADO; b) média entre 5.0 e 6.9:
RECUPERAÇÃO e c) média 7.0 ou superior: APROVADO.'''

n1=float(input('Qual o valor da primera nota: '))
n2=float(input('Qual o valor da segunda nota: '))
x=(n1+n2)/2
if x>7:
    print('Media {} aprovado'.format(x))
elif x>=5 and x<=6.9:
    print('Media {} recupreção'.format(x))
elif x>5:
    print('Media {} reprovado'.format(x))