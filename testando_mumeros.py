'''Ex 5. Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa
deve apresentar o seguinte menu:
1. Média ponderada, com pesos 2 e 3, respectivamente.
2. Quadrado da soma dos 2 números.
3. Cubo do menor número.
Escolha uma opção:
De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a
opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado.
4'''

v1=float(input('Informe o primeiro valor : '))
v2=float(input('Informe o segundo valor : '))
x=float(input('Escolha uma opção: \n 1: Media ponderada \n 2: Quadrado da soma dos 2 números \n 3: Cubo do menor nnúmero     '))

if x<=0 or x>=4:
    print('opção invalida! ')
else:
    if x==1:
        mp=(v1*2+v2*3)/5
        print('{:.2f}'.format(mp))
    else:
        if x==2:
            q=(v1+v2)**2
            print('Quadrado da soma edesses valores é: {} '.format(q))
        else:
            if x==3:
                if v1>v2:
                    c=(v2)**3
                    print('Cubo do menor número é {} '.format(c))
                else:
                    C=(v1)**3
                    print('Cubo do menor número é {} '.format(C))