'''Ex 5. Uma loja de roupas está vendendo camisas básicas com descontos, mas seus funcionários têm
dificuldades no cálculo do valor final a ser cobrado. Por isso, seu Tanaka, dono da loja, convidou você
para criar um programa para calcular o preço final a partir do número de camisas. Seu Tanaka definiu as
seguintes regras de desconto: a) Até 5 camisas, desconto de 3%; b) Acima de 5 camisas e até 10
camisas, desconto de 5%; c) Acima de 10 camisas, desconto de 7%.'''

from doctest import debug_script


x=float(input('Quantas camisas foram vendidas? '))
y=float(input('O valor da camisa vendida: '))
if x<=5:
    des_a=y*0.03
    a=y-des_a
    final_a=(x*a)
    print(' O desconto por unidade saio pelo valor de R${} e o total deu {} '.format(a, final_a))
elif x>5 and x<=10:
    des_b=y*0.05
    b=y-des_b
    final_b=x*b
    print('O desconto por unidade saio pelo valor de R${} e o total deu {}'.format(b, final_b))
elif x>10:
    des_c=y*0.07
    c=y-des_c
    final_c=x*c
    print('O desconto por unidade saio pelo valor de R${} e o total deu {}'.format(c, final_c))