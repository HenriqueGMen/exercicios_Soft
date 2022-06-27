class ComplexNumbers:
    
    def calcular_complexos(a, b, c):
        n1 = complex(a)
        n2 = complex(b, c)
        n3 = complex(c, a)
    
        adicao = n1 + n2 + n3
        print("Adição =", adicao)
        print("Parte Real:", adicao.real)
        print("Parte Imaginária:", adicao.imag)
    
        sub = n1 - n2 - n3
        print("Subtração =", sub)
        print("Parte Real:", sub.real)
        print("Parte Imaginária:", sub.imag)
    
        mult = n1 * n2 * n3
        print("Multiplicação =", mult)
        print("Parte Real:", mult.real)
        print("Parte Imaginária:", mult.imag)
    
        div = n1 / n2 / n3
        print("Divisão =", div)
        print("Parte Real:", div.real)
        print("Parte Imaginária:", div.imag)
    
    print(calcular_complexos(6, 2, 4))
