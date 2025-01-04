import pytesseract
from PIL import Image

# Open the image file
PS = "FUVEST 2025"
image1 = Image.open(f'image1{PS}.png')
image2 = Image.open(f'image2{PS}.png')

# Perform OCR using PyTesseract
text1 = pytesseract.image_to_string(image1)
text2 = pytesseract.image_to_string(image2)

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

notasStr = []
rankStr = []

if PS == "ENEM-USP 2024":
     [notasStr,rankStr] = ENEMUSP(text1, text2)
elif PS == "FUVEST 2025":
     [notasStr,rankStr] = FUVEST(text1, text2)
elif PS == "Ingresso na USP via Competições do Conhecimento 2025":
     [notasStr,rankStr] = CompConhecimento(text1, text2)
else:
     [notasStr,rankStr] = ProvaoPaulista(text1, text2)

print(notasStr)
print(rankStr)