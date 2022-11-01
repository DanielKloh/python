'''Ex 3. Escreva um programa que solicite ao usuário a estatura de 3 pessoas. Ao fim, o programa deve
imprimir as estaturas em ordem decrescente. Utilize os conceitos de estruturas condicionais para
solucionar esse exercício'''

p1=float(input('Digite a estatura da primei pessoa: '))
p2=float(input('Digite a estatura da segunda pessoa: '))
p3=float(input('Digite a estatura da terceira pessoa: '))
if p1>p2 and p1>p3 and p2>p3:
    print('{} é o menor {} é o do meio e {} é o maior '.format(p3, p2, p1))
elif p1>p3 and p1>p2 and p3>p2:
    print('{} é o menor {} é o do meio e {} é o maior '.format(p2, p3, p1))
elif p2>p1 and p2>p3 and p3>p1:
    print('{} é o menor {} é o do meio e {} é o maior '.format(p1, p3, p2))
elif p2>p3 and p2>p1 and p1>p3:
    print('{} é o menor {} é o do meio e {} é o maior '.format(p3, p1, p2))
elif p3>p1 and p3>p2 and p2>p1:
    print('{} é o menor {} é o do meio e {} é o maior '.format(p1, p2, p3))
elif p3>p1 and p3>p2 and p1>p2:
    print('{} é o menor {} é o do meio e {} é o maior '.format(p2, p1, p3))