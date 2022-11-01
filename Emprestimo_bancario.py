'''Ex 1. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação
mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa=float(input('Digite o valor da casa que pretende comprar: '))
salario=float(input('Digite o valor do seu salario: '))
ano=float(input('Informe em quantos anos pretende pagar: '))
ano2=ano*12
prestacao=casa/ano2
sal=(salario*0.3)
if prestacao > sal:
    print('fora')
else:
    print('vai nessa')
