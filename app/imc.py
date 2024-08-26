nomePaciente = input("Digite o nome do paciente ")
peso = float(input("Digite o peso do paciente(kg) "))
altura = float(input("Digite a altura do paciente(cm) "))
    

def calcImc(peso, altura):
    altura /= 100
    imc = peso / (altura*altura)
    return  print("O imc do paciente ",nomePaciente," é", imc)

calcImc(peso,altura)