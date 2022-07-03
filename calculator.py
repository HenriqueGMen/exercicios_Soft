def calculadora(num1, num2, operador):

    if operador <= 0 or operador > 4:
        return print(0)

    elif operador == 1:
        return print('A soma de', num1, 'é', num2, '=', num1 + num2)

    elif operador == 2:
        return print('o resultado da subtração entre', num1, 'é', num2, '=', num1 - num2)

    elif operador == 3:
        return print('o resultado da multiplicação entre', num1, 'é', num2, '=', num1 * num2)

    elif operador == 4:
        return print('o resultado da divisão entre', num1, 'é', num2, '=', num1 // num2)
        
        
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
    
print('Escolha a operação desejada:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
    
operador = int(input('Qual a operação desejada?'))

calculadora(num1, num2, operador)
