'''Ex 2. Crie um programa que leia o nome de uma pessoa e diga se ela tem “DIAS” no nome'''

nome=input('digite o seu nome: ').lower()
x='dias' in nome
if x==True:
    print('Essa pessoa tem Dias no nome')
else:
    print('Essa pessoa não tem Dias no nome')

#ou 
#nome=input('digite o seu nome: ').strip()
#print('seu nome tem Dias? {}'.format('DIAS' in nome.power()))