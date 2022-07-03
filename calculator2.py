def calculadora(num1, num2, operador):

    if operador == 1:
        return print('A soma de', num1, 'é', num2, '=', num1 + num2)

    elif operador == 2:
        return print('o resultado da subtração entre', num1, 'é', num2, '=', num1 - num2)

    elif operador == 3:
        return print('o resultado da multiplicação entre', num1, 'é', num2, '=', num1 * num2)

    elif operador == 4:
        return print('o resultado da divisão entre', num1, 'é', num2, '=', num1 // num2)

while True:    
    print('Escolha a operação desejada:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')

    operador = int(input('Qual a operação desejada?'))
    if operador < 0 or operador > 4:
        print('Opção inválida. Digite novamente:')
        continue
  
    elif operador == 0:
        print('Programa finalizado. Até mais.')
        break
    
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    calculadora(num1, num2, operador)
