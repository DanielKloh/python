#.Le um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

'''Ex 5. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
separados. Ex.: Digite um número: 1834. unidade: 4 dezena: 3 centena: 8 milhar: 1.
'''

num=input('digite um número com 4 dígitos: ')
u=num[3]
d=num[2]
c=num[1] 
m=num[0]
print('Assinalando o número {} podemos indentificar a unidade {}, adezena {}, a centena {}, e o milhar {}'.format(num, u, d, c, m))