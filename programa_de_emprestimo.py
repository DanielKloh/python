
print('programa de emprestimo ## \n responda 0 - não e 1 - sim ')
nomen=int(input('Possue um nome negativado? '))
if nomen == 1:
    print('não pode realizar o emprestimo!' )
else:
    cart=int(input('Possue carteira assinada? '))
    if cart == 0:
        print('não pode realizar o emprestimo!' )
    else:
        casa=int(input('Possue casa propia? '))
        if casa == 0:
            print('Não pode realizar o emprestimo! ')
        else:
            print('Emprestimo concedido')
