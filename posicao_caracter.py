'''Ex 8. Faça um programa que leia uma frase pelo teclado e mostre: a) Quantas vezes aparece a
letra “A”. b) Em que posição ela aparece a primeira vez. c) Em que posição ela aparece a última
vez.'''

x=input('Digite uma frase: ').lower()
a=x.count('a')
print('A letra a se repete {} veses'.format(a))
b=x.find('a')+1
print('A letra a aparece na posição {} pela primeira vez'.format(b))
c=x.rfind('a')+1
print('A letra a aparece pela ultima vez na posição {} '.format(c))