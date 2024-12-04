import pytesseract
from PIL import Image

# Open the image file
image1 = Image.open('image1.png')
image2 = Image.open('image2.png')

# Perform OCR using PyTesseract
text1 = pytesseract.image_to_string(image1)
text2 = pytesseract.image_to_string(image2)
if("Modalidade de ingresso" in text2):
    notas = text1
    classificacoes = text2
else:
    notas = text2
    classificacoes = text1

notasStr = (notas[notas.find("Redac3o")+7:notas.find("Maximo")]).strip().split("\n\n")

rankStr = []
for i in (classificacoes[classificacoes.find("carreira")+8::]).strip().split("\n"):
        if i.isnumeric():
            rankStr.append(i)



print(notasStr)
print(rankStr)