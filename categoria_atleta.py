'''Ex 6. Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que
auxilie os seus eletricistas no cálculo das principais grandezas da eletricidade que são Tensão, Resistência e
Corrente. Sabe-se que U=Ri, onde, U é a Tensão (em V), R é a Resistência (em Ώ) e i a Corrente (em A). Você foi
contratado(a) pela empresa para atender a essa solicitação. Construa um programa que apresente o seguinte menu:
************************************************
CÁLCULO DE GRANDEZAS ELÉTRICAS
************************************************
1. Tensão (em Volt)
2. Resistência (em Ohm)
3. Corrente (em Ampére)
************************************************
Qual grandeza deseja calcular?
Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o
cálculo. Quando o eletricista escolher: a) Tensão, o programa deve solicitar que ele informe os valores da
Resistência e da Corrente b) Resistência, o programa deve solicitar que ele informe os valores da Tensão e da
Corrente c) Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência. Por fim, o
programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.'''

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