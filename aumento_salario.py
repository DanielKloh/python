'''Ex 7. Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o
cargo, conforme a tabela abaixo:
Crie um programa que solicite ao usuário o salário e o cargo de um determinado funcionário. Na
sequência, o programa deve calcular e imprimir o seu novo salário. Caso o cargo informado não esteja
na tabela, o programa deve imprimir “Cargo inválido”.'''

sal=float(input('Informe o salario do funcionario: '))
cargo=float(input('Informe o cargo do funcionario:\n 1:Programador de Sistemas\n 2:Analista de Sistemas\n 3:Analista de Banco de Dados  '))

if cargo<1 or cargo>3:
    print('cargo invalido')

if cargo==1:
    salf=(sal*0.30)+sal
    print('O seu novo salario é de R${:.2f} '.format(salf))
elif cargo==2:
    salf= (sal*0.20)+sal
    print('O seu novo salario é de R${:.2f} '.format(salf))
elif cargo==3:
    salf=(sal*0.15)+sal
    print('O seu novo salario é de R${:.2f} '.format(salf))