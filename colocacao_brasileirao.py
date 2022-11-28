'''Ex 2. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão na ordem de
colocação. Depois mostre:a) os cinco primeiros b) os últimos 4 colocados c) times em ordem alfabética
e d) em que posição está o time Chapecoense'''

lista=['Palmeiras','Chapecoense','Vasco da Gama','Grêmio','Flamengo', 'Corinthians','Internacional','Cruzeiro','São Paulo','Atlético Mineiro','Botafogo','Fluminense','Coritiba','Bahia','Goiás','Guarani','Sport','Portuguesa','Atlético Paranaense','Vitória']

# 5 primeiros
primeiros5=lista[:5]

# 4 ultimos
ultimos4=lista[-4:]

#chapecoense
chapeco=lista.index('Chapecoense')

#times em ordem alfabetica
lista.sort()
ordem = lista

# impresão
print(f'5 primeiros{primeiros5}')
print(f'ultimos 4 blocos{ultimos4}')
print(f'lista de times em ordem alfabetica: {ordem}')
print(f'chapecoense esta na posição {chapeco}')
