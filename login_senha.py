'''Ex 9. Suponha que o professor Fábio possui 2 logins na rede acadêmica da instituição. Construa
um programa que valida o acesso do professor à rede. Caso o usuário/senha informado esteja
correto, o programa deve imprimir a mensagem “Seja bem vindo!”. Caso contrário, “Usuário e
senha não conferem”.'''

log1=input('Digite o login: ')
senha1=input('Digite a senha: ')

log2=('Daniel@omelhor')
senha2=('123')

log3=('Daniel@eu')
senha3=('jkl')

if log1==log2 and senha1==senha2:
    print('Seja bem vindo')
elif log1==log3 and senha1==senha3:
    print('Seja bem vindo')
else:
    print('usuario e senha não conferem')