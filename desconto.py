'''Ex 4. Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço
normal e condição de pagamento: a) à vista dinheiro/cheque: 10% de desconto; b) à vista no cartão: 5%
de desconto; c)em até 2x no cartão: preço normal.'''

x=float(input('Qual o vaor do produto '))
xx=float(input('selecione o metudo de pagamento##\n 1:Á vsta/cheque\n 2:Á vista no cartão\n 3:Em até 2x no catão\n '))
if xx==1:
    aa=x*0.10
    a=x-aa
    print('O valor a vista ficou R${:.2f} '.format(a))
elif xx==2:
    bb=x*0.05
    b=x-bb
    print('O valor á vista no catão ficou R${:.2f} '.format(b))
elif xx==3:
    print('O valor em 2x no cartão ficou R${:.2f} '.format(x))
else:
    x>=4 and x<=0
    print('OPÇÃO INVALIDA!!!')