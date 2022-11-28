'''Ex 3. Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua
cerimônia de formatura. Construa um programa para cadastrar os nomes das pessoas que compraram a
rifa. Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.'''


from random import choice
lista=[]


nome=(input("Para encerar digite 'fim'\nDigite um nome: "))

while nome != 'fim':
    nome=(input("Digite um nome: "))
    lista.append(nome)
    

sorteio=choice(lista)
print(f"O ganhador foi {lista[0]}")

