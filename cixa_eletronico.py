'''Ex 3. Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista
para validar o seu acesso ao sistema. Considere que a senha fictícia do correntista é 123456. Considere as
seguintes restrições: a) quando a senha estiver correta, mostrar a mensagem: “Olá, <SEUNOME>. Seja
bem-vindo ao nosso banco!" b) quando o usuário errar a senha pela primeira vez, mostrar a mensagem:
“Senha incorreta! Você ainda tem 2 tentativas.” c) se o usuário errar a senha pela segunda vez, mostrar a
mensagem: “Senha incorreta! Você ainda tem 1 tentativa.” d) se o usuário errar a senha novamente,
mostrar a mensagem “Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.” e o programa
deve ser encerrado. '''



erros=0
for c in range(3,0,-1):
    senha=int(input('Senha:'))
    if senha== 123456:
        print('Bem vindo!')
        break
    elif senha !=123456:
        print('senah incoreta {} tentativa'.format(c-1))
        if c==1:
            print('senha bloqueada')
            break