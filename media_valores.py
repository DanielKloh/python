'''Ex 3. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.'''

soma=1
total=0

n=int(input('Digite um numero inteiro '))
maior=n
menor=n
total+=n

while True:
    n=int(input('Digite um numero inteiro '))
    total+=n
    if maior<n:
        maior=n
    if menor>n:
        menor=n
    soma+=1
    continuar=input('Quer continuar[S/N] ').strip().upper()
    if continuar=='N':
        break

media=total/soma
print('A media desses valores é {}, {} é o maior e {} é o menor'.format(media,maior,menor))