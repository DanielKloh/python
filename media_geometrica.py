'''Ex 5. Crie um programa que declare uma lista L, a qual você pode preenchê-la manualmente. Em
seguida, o programa deve calcular a média geométrica entre o menor e o maior elemento da lista L. Ao
fim, o programa deve imprimir a média geométrica encontrada.'''


from math import sqrt

lista=[9,3,5,7,2,1]

menor=min(lista)
maior=max(lista)
media_geo=sqrt(menor*maior)

print(f'Lista: {lista}')
print(f'Média geométrica entre {menor} e o {maior} elemento é igual a {media_geo}') 