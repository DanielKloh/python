'''Ex 3. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
status, de acordo com: a) até 18.5: abaixo do peso; b) entre 18.5 e 25: peso ideal; c) 25 até 30:
sobrepeso; d) 30 até 40: obesidade e e) acima de 40: obesidade mórbida.'''

peso=float(input('Qual deu peso (em KG) ? '))
altura=float(input('Qual a sua altura (em metros) ? '))
imc=peso/(altura**2)
if imc<18.5:
    print('abaixo do peso')
elif imc>18.5 and imc<25:
    print('peso ideal')
elif imc>25 and imc <30:
    print('sobrepeso')
elif imc>30 and imc<40:
    print('obesidade')
elif imc>=40:
    print('obesdade morbida')                                     