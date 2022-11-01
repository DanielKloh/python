'''Ex 6. Crie um programa no qual o usuário informe o código do cargo de um funcionário 
e o seu respectivo salário. Para encerrar a leitura dos dados, defina uma condição de parada (por
exemplo, código do cargo igual a zero). Ao fim, o programa deve informar a média salarial dos
nutricionistas.
'''


from tkinter import N


print('Codigo de cargo:\n  1:Enfermeiro\n 2:Nutricionistan\n 3:Medico')

qtdnutri=0
total_sal_nutri=0

while True:
    cargo=int(input('informe o codigo de um cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('Salario R$: '))
        if cargo ==2:
            qtdnutri+=1
            total_sal_nutri+=salario

        resp=input('Deseja contunuar [S/N]: ').upper
        if resp()=='N':
            break
    else:
        print('Codigo invalido!')

if qtdnutri>0:
    media=total_sal_nutri/qtdnutri
    print(f'Media dos salarios dos nutricionistas R$: {media:.2f}')
else:
    print('Não foram inseidas dados sobre as nutricionistas')