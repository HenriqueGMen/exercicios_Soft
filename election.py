candidato_X = 0
candidato_Y = 0
candidato_Z = 0
branco = 0
cont = 'sim'

while (cont == 'sim'):
    print('Votação iniciada')
    print('Digite 889 para votar no candidato X')
    print('Digite 847 para votar no candidato Y')
    print('Digite 515 para votar no candidato Z')
    print('Digite 0 para votar em branco')
    
    try:
        voto = int(input("Digite seu voto: "))
        
        if (type(voto) == int):
            if voto == 889:
                candidato_X += 1
            elif voto == 847:
                candidato_Y += 1
            elif voto == 515:
                candidato_Z += 1
            elif voto == 0:
                branco += 1
            else:
                branco += 1
        else:
            raise Exception('Digite um número...')
            
    except:
        print('Digite um número válido')
        continue
    
    cont = input('Digite sim para registrar outro voto e nao para encerrar votação. ')
    if (cont == 'nao'):
        break
        
if(candidato_X > candidato_Y and candidato_X > candidato_Z):
    print('O vencedor foi o candidato X')
elif(candidato_Y > candidato_Z):
    print('O vencedor foi o candidato Y')
else:
    print('O vencedor foi o candidato Z')
    
print('Candidato X:', candidato_X, 'votos')
print('Candidato Y:', candidato_Y, 'votos')
print('Candidato Z:', candidato_Z, 'votos')
print('Brancos e nulos:', branco, 'votos')
