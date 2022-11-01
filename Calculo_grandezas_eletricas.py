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


x=float(input('*****************************************************************\nCÁLCULO DE GRANDEZAS ELÉTRICAS \n***************************************************************** \n 1. Tenção (em volt)\n 2. Resistencia (em ohm)\n 3. Corrente (em Ampére) \n*****************************************************************\n Qual grandeza deseja calcular? '))
if x<1 or x>4:
    print('Opção invalida')
elif x==1:
    res=float(input('informe a resistencia: '))
    cor=float(input('informe a corrente: '))
    fim=res*cor
    print('A tençãovale {} Volt '.format(fim))
elif x==2:
    ten=float(input('informe o valor da tenção: '))
    core=float(input('informe a resistencia: '))
    resi=ten/core
    print('A corrente {} Ohm '.format(resi))
elif x==3:
    tenc=float(input('informe o valor da tenção: '))
    resis=float(input('informe a resistencia: '))
    corrente=tenc/resis
    print('A corrente vale {} Ampére '.format(corrente))