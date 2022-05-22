#-*- coding:utf8 -*-
from src.Content import Content

class Write:
    def __init__(self, file):
        self.file = file
        self.filename = self.file.split('.')[0]
        self.ext = self.file.split('.')[-1]
        self.content = Content()
        
    # Leer archivo separado por saltos de linea
    def writeFile(self):
        if self.ext == 'txt':
            file = open(self.file, 'w+')
            # Agregar indice a cada dato leido
            
            return self.content
        else:
            return 'El archivo no tiene un formato valido'