'''Ex 2. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

soma=0
qtd=0

while True:
    num=int(input('Digite um número inteiro: '))
    if num>0 and num<1000:
        soma+=num
        qtd+=1
    else:
        break
print('A soma dos {} numeros digitatdos é {} '.format(qtd, soma))