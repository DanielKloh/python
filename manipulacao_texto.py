#Le o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas e todas minúsculas, quantas letras ao todo (sem considerar
#espaços) e quantas letras tem o primeiro nome.
'''Ex 4. Crie um programa que leia o nome completo de uma pessoa e mostre: a) O nome com
todas as letras maiúsculas e todas minúsculas. b) Quantas letras ao todo (sem considerar os
espaços). c) Quantas letras tem o primeiro nome.'''

nome=input('Digite o seu nome completo ')
m=nome.upper()
print('Seu nome em letra maiuscula é {}'.format(m))
mm=nome.lower()
print('seu nome com letras minusculas é {}'.format(mm))
sem_space=len(nome)-nome.count(' ')
print('Seu nome tem {} letras '.format(sem_space))
primeiro=nome.find(' ')
print('Seu primeiro nome tem {} letras '.format(primeiro))
