#-*- coding:utf8 -*-
from src.Content import Content

class Write:
    def __init__(self, file, content):
        self.file = file
        self.filename = self.file.split('.')[0]
        self.ext = self.file.split('.')[-1]
        self.content = content
        
    # Leer archivo separado por saltos de linea
    def writeFile(self):
        """ Escribir archivo enviado en el constructor """
        if self.ext == 'txt':
            file = open(self.file, 'w+')
            file.write(self.content)
            file.close()
            return self.content
        else:
            return 'No se puede escribir el archivo'
        
