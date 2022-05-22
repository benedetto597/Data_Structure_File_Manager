#-*- coding:utf8 -*-
import re
from src.Read import Read
from src.Menu import Menu

# Leer el contenido del archivo
read = Read("data/Proyecto1.txt")

# Imprimir el contenido del archivo con Tabulate
end = False
menu = Menu()
menu.printIntro()
read.readFile()
read.content.printAll()

while (end == False):
    option = menu.printOpts()
    if option == False:
        end = True
    elif option == '1':
        read.content.printAll()
    elif option == '2':
        index = input("\n***** Insert index of a record: *****\n")
        read.content.printDetail(index)
