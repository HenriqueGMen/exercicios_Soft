def calcularIdade(anoNasc, anoAtual):
    
    if (anoNasc > 1922 and anoNasc < 2021):
        idade = anoAtual - anoNasc
    else:
        raise Exception('Ano de nascimento inválido. Tente novamente...')
    return idade

while True:
    print('Vamos descobrir sua idade...')

    try:
        nome = (input('Digite seu nome:'))
        anoAtual = int(input('Informe o ano atual:'))
        anoNasc = int(input('Informe o ano em que você nasceu:'))
        
        idade = calcularIdade(anoNasc, anoAtual)
        print(nome, ', Você tem', idade, 'anos.')
        break
    
    except ValueError:
        print('Digite um ano válido...')
    
    except Exception as e:
        print(e)
        continue
