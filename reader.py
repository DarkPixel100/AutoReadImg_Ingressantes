# Imports
import pytesseract as pytss
import downloader
from PIL import Image

# Funções auxiliares
def decide(containsFactor, doesntContainF, factor):
     if(factor in containsFactor): return [containsFactor,doesntContainF]
     return [doesntContainF,containsFactor]

def ENEMUSP(t1, t2):
     [notas, classificacoes] = decide(t1, t2, "Redacao")
     notasFinalStr = (notas[notas.find("Pontos")+6:notas.find("Maximo")]).strip().split("\n\n")
     resultsFinalStr = [];

     temp = (classificacoes[classificacoes.find("1")+8::]).strip().split("\n")
     for i in temp:
          if i.isnumeric(): resultsFinalStr.append(i)
     return [notasFinalStr,resultsFinalStr]

def FUVEST(t1, t2):
     [classificacoes, notas] = decide(t2, t1, "Modalidade de ingresso")
     notasFinalStr = (notas[notas.find("Redac3o")+7:notas.find("Maximo")]).strip().split("\n\n")
     resultsFinalStr = [];

     temp = (classificacoes[classificacoes.find("carreira")+8::]).strip().split("\n")
     for i in temp:
          if i.isnumeric(): resultsFinalStr.append(i)
     return [notasFinalStr,resultsFinalStr]

def CompConhecimento(t1, t2):
     [notas, classificacoes] = decide(t1, t2, "Resultado")

     notasFinalStr = []
     resultsFinalStr = []

     tempNotas = (notas[notas.find("Pontos")+6::]).strip().split("\n")
     tempResults = (classificacoes[classificacoes.find("1")+8::]).strip().split("\n")
     for i in tempNotas:
          notasFinalStr.append(i[i.find("curso")+6::])
     for i in tempResults:
          if i.isnumeric(): resultsFinalStr.append(i)

     return [notasFinalStr,resultsFinalStr]

def ProvaoPaulista(t1, t2):
     return

# Função de extração dos dados das imagens
def getScreenshotValues(PS, url1, url2):
     # image1_data = requests.get(url1 + "&export=download", stream=True)
     # image2_data = requests.get(url2 + "&export=download", stream=True)
     
     # image1 = Image.open(io.BytesIO(image1_data.content))
     # image2 = Image.open(io.BytesIO(image2_data.content))

     # Perform OCR using PyTesseract
     text1 = pytss.image_to_string(image1)
     text2 = pytss.image_to_string(image2)

     notasStr = []
     rankStr = []

     if PS == "ENEM-USP 2025":
          [notasStr,rankStr] = ENEMUSP(text1, text2)
     elif PS == "FUVEST 2025":
          [notasStr,rankStr] = FUVEST(text1, text2)
     elif PS == "Ingresso na USP via Competições do Conhecimento 2025":
          [notasStr,rankStr] = CompConhecimento(text1, text2)
     else:
          [notasStr,rankStr] = ProvaoPaulista(text1, text2)

     print(notasStr)
     print(rankStr)
     return [notasStr, rankStr]