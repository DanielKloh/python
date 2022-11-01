'''Ex 1. Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo'''

from time import sleep
c=1
for c in range(9,-2,-1):
    c+=1
    sleep(1)
    print(c)
print('FELIZ ANO NOVO!!!')