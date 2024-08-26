try:
    temperature = float(input("Digite alguma coisa: "))

    if temperature < 7.0:
        print("Congelou!")
    elif temperature < 10.0:
        print("Frio!")
    elif temperature < 26.0:
        print("Ótimo!")
    else:
        print("Muito quente!")
        
except ValueError:
    print("Erro: valor inválido.")
