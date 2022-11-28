'''Ex 1. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
mostre: a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3 e c) quais
foram os números pares.'''


par=[]

valor1 = float(input('Informe  o valor 1: '))
valor2 = float(input('Informe  o valor 2: '))
valor3 = float(input('Informe  o valor 3: '))
valor4 = float(input('Informe  o valor 4: '))

lista=(valor1, valor2, valor3, valor4)


#conta quantas vezes o número 9 se repete
lista1=lista.count(9)




#quantas vezes foram digitados o valor 3
primeiro_valor=lista.index(3)




#números pares
for c in lista:
    if c%2==0:
        par.append(c)
        print(f'O número {c} é par')
        


#impresão dos valores
print(f'Digito {lista1} o númeor 9, o número 3 aparece na prinmeira vez na posição {primeiro_valor}.')