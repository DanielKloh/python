'''Ex 7. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
esteja errado, peça a digitação novamente até ter um valor correto.'''

s=input('Informa seu sexo, M ou F: ').strip().upper()
while s not in 'MF':
    s=input('Dados invalidos. Por favor, informe seu sexo [M/F]: ').strip().upper()
print('Sexo {} registrado com sucesso!!!'.format(s))