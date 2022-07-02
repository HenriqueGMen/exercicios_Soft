aluno = input( 'Digite seu nome: ')
nota1 = float(input( 'Digite sua primeira nota: '))
nota2 = float(input( 'Digite sua segunda nota: '))
faltas = int(input('Quantidade de faltas: '))

media = (nota1 + nota2) / 2

print(aluno, "sua média foi: ", media)

if (media < 7):
    print("Reprovado")
elif (media >= 7 and faltas > 3):
    print("Reprovado por falta")
else:
    print("Aprovado por média")
