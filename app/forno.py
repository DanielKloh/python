# Leitura dos dados iniciais
umidade = float(input('Digite o percentual de umidade no ar: '))
tempExterna = float(input('Digite o valor da temperatura externa: ')) 

# Situação de Inverno, iniciar desumidificação
if umidade >= 40 and tempExterna <= 20:
    print("INÍCIO DESUMIDIFICAÇÃO")
    tempInterna = float(input('Digite o valor da temperatura interna: ')) 
    umidadeInterna = float(input('Digite o percentual da umidade interna: ')) 

    if tempInterna < 15: 
        print('Aquecendo a 100 graus celsius')
        print('Ligando o exaustor')
    else:
        print("Situação não requer aquecimento.")
    # Adicionar aqui mais instruções conforme necessário para desumidificação

# Situação de clima diverso, iniciar cocção
else:
    print("INICIANDO COCÇÃO")
    umidadeInterna = float(input('Digite o percentual da umidade interna: ')) 
    
    if umidadeInterna > 15:
        print("Ligando o exaustor")
    
    tempInterna = float(input('Digite o valor da temperatura interna: ')) 
    
    if tempInterna < 200: 
        print('Aquecendo a 380 graus celsius')
    else:
        print('Temperatura adequada, mantendo estado.')
    # Adicionar aqui mais instruções conforme o procedimento de cocção

print("Processo finalizado.")
