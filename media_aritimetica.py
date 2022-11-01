'''Ex 5. Crie um programa no qual o usuário informe a idade de um número indeterminado de alunos. Para
encerrar a leitura dos dados, o usuário deve informar uma idade negativa. No final, o programa deve
mostrar a média aritmética entre a maior e a menor idade.'''


idade=int(input('idade: '))

maisnovo=idade
maisvelho=idade

while True:
    idade=int(input('idade: '))
    if idade<0:
        break

    if idade<maisnovo:
        maisnovo=idade
    elif idade>maisvelho:
        maisvelho=idade

media=(maisnovo+maisvelho)/2

print(f'menor idade: {maisnovo} \nMaior idade: {maisvelho}\nMedia das idades = {media:.2f}')