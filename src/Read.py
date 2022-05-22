#-*- coding:utf8 -*-
from src.Content import Content

class Read:
    def __init__(self, file):
        self.file = file
        self.filename = self.file.split('.')[0]
        self.ext = self.file.split('.')[-1]
        self.content = Content()
        
    # Leer archivo separado por saltos de linea
    def readFile(self):
        if self.ext == 'txt':
            file = open(self.file, 'r')
            # Agregar indice a cada dato leido
            for count, value in enumerate(file.readlines()):
                self.content.addRecord(count, value.replace('\n', ''))
            file.close()
            return self.content
        else:
            return 'El archivo no tiene un formato valido'