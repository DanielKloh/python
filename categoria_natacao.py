'''Ex 1. A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade: a) até 9 anos: MIRIM; b) até 14 anos: INFANTIL; c)
até 19 anos: JUNIOR d)até 25 anos: SÊNIOR; e) acima:MATER.
'''

from datetime import date
atual=date.today().year
ano=int(input('Qual a no nasceu'))
x=atual-ano

if x<=9:
    print('MiIRIM')
elif x>9 and x<14:
    print('INFANTIL')
elif x>14 and x<19:
    print('JUNIOR')
elif x>19 and x<=25:
    print('SENIOR')
elif x>25:
    print('MATER')