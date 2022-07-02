print("Vamos descobrir em qual categoria de habilitação você se enquadra...")

rodas = int(input("Veículo com quantas rodas?"))
peso = int(input("Qual o peso do veículo em kg?"))
quant_pessoas = int(input("Quantas pessoas o veículo suporta transportar?"))

if rodas <= 3:
    print('Categoria A')
elif rodas == 4 and peso <= 3500 and quant_pessoas <= 8 :
    print('Categoria B')
elif rodas >= 4 and peso <= 6000:
    print('Categoria C')
elif rodas >= 4 and quant_pessoas > 8:
    print('Categoria D')
else:
    print('Categoria E')
