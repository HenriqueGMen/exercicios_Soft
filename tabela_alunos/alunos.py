import pandas as pd

tabela = pd.read_csv("notas_alunos.csv", sep=",")

tabela["media"] = (tabela["nota_1"] + tabela["nota_2"]) / 2

tabela.loc[(tabela["media"] >= 7) & (tabela["faltas"] <= 5), "situacao"] = "Aprovado"
tabela.loc[(tabela["media"] < 7) | (tabela["faltas"] > 5), "situacao"] = "Reprovado"

tabela.to_csv("alunos_situação.csv")

maior_falta = tabela["faltas"].max()
print("O maior número de faltas foi:", maior_falta)

maior_media = tabela["media"].max()
print("A maior média foi:", maior_media)

media_geral = tabela["media"].mean()
print("A média geral da turma foi:", media_geral)