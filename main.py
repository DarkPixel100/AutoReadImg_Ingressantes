import pandas as pd
import reader

# Main
mainDF = pd.read_csv('TESTE_  Dados - Ingressantes (respostas) - Respostas ao formulário 1.csv')
# print(mainDF.to_string()[1233::])

enemDF = mainDF[mainDF["Entrou por qual processo seletivo?"] == "ENEM-USP 2025"]
fuvestDF = mainDF[mainDF["Entrou por qual processo seletivo?"] == "FUVEST 2025"]
compConhecimentoDF = mainDF[mainDF["Entrou por qual processo seletivo?"] == "Ingresso na USP via Competições do Conhecimento 2025"]
# provPaulistaDF = mainDF[mainDF["Entrou por qual processo seletivo?"] == "Provão Paulista 2025"]

# modosDeIngresso = [enemDF, fuvestDF, compConhecimentoDF]

# Teste atual com FUVEST 2025
for i in range(len(fuvestDF)):
     dataArray = {"notas":[], "classif":[]}
     url1 = ''
     url2 = ''
     for j in range(13):
          cell = fuvestDF.iat[0, 12+j]
          if j <= 4: dataArray["notas"].append(cell)
          elif j == 5: url1 = cell
          elif j <= 11: dataArray["classif"].append(cell)
          else: url2 = cell
     reader.getScreenshotValues("FUVEST 2025", url1, url2)
     