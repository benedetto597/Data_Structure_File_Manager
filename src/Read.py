#-*- coding:utf8 -*-
from src.Content import Content

class Read:
    def __init__(self, file, content):
        self.file = file
        self.filename = self.file.split('.')[0]
        self.ext = self.file.split('.')[-1]
        self.content = content
        
    # Leer archivo separado por saltos de linea
    def readFile(self):
        """ Leer archivo enviado en el constructor """
        if self.ext == 'txt':
            file = open(self.file, 'r')
            # Agregar indice a cada dato leido
            arrContent = file.readlines()
            if len(arrContent) > 0:
                for count, value in enumerate(arrContent):
                    self.content.addRecord(count, value.replace('\n', ''))
                file.close()
                return self.content
            else:
                file.close()
                print("\n***** El archivo esta vacio *****\n")
                return False
        else:
            print("\n***** El archivo no es extension .txt *****\n")
            return False