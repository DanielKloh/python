'''Ex 3. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os salários inferiores ou iguais
a R$1250,00, o aumento é de 15%'''

x=float(input('Informe o salario atual: '))
if x>1250:
    x1=(x*0.10)+x
    print('O seu  aumento é de ''10%'' e o salario sera de R${:.2f} '.format(x1))
else:
    x2=(x*0.15)+x
    print('O seu  aumento é de ''15%'' e o salario sera de R${:.2f} '.format(x2))