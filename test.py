import easyocr
from easyocr import Reader
reader = easyocr.Reader() # this needs to run only once to load the model into memory
result = reader.readtext('D:/Documents/documents 2024/neural networks/code/EasyOCR2/examples/windowsPart.png')
print(result)