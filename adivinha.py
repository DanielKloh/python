'''Ex 5. Melhore o exercício Ex 1 da Aula 6 onde o computador vai “pensar’ em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
vencer.'''

from operator import truediv
from random import randint

computador = randint(0,10)

print('Pense em um número de 0 a 10')

acertou = False
palpites=0

while not acertou:
    jogador=int(input('Qual o seu palpite? '))
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador>computador:
            print('menos... Tente novamente! ')
print('Acertou com {} tentativas. Parabéns!!!'.format(palpites))
