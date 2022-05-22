#-*- coding:utf8 -*-
from multiprocessing import cpu_count
import re
from src.Read import Read
from src.Write import Write
from src.Menu import Menu
from src.Content import Content

# Leer el contenido del archivo
content = Content()
read = Read("data/Proyecto1.txt", content)

# Imprimir el contenido del archivo con Tabulate
menu = Menu()
menu.printIntro()
read.readFile()
content.printAll()

end = False

while (end == False):
    option = menu.printOpts()
    if option == False:
        print("\n***** Saliendo... *****\n")
        end = True
    elif option == '1':
        content.printAll()
    elif option == '2':
        index = input("\n***** Insert index of a record: *****\n")
        content.printDetail(index)
    elif option == '100':
        oldContent = content
        value = input("\n***** Insert value to add a record: *****\n")
        content.addRecord(content.records.getLast().index + 1, value)
        write = Write("data/Proyecto1.txt", content.stringLLate(content.records))
        write.writeFile()
        content = Content()
        read = Read("data/Proyecto1.txt", content)
        read.readFile()
        content.printAll()
        content.updateAvaibles(oldContent)
        write = Write("data/Availables.txt", content.stringLLate(content.availables))
        write.writeFile()
    elif option == '101':
        oldContent = content
        index = input("\n***** Insert index to add a record: *****\n")
        value = input("\n***** Insert value to add a record: *****\n")
        content.addRecordInPosition(int(index), value)
        write = Write("data/Proyecto1.txt", content.stringLLate(content.records, int(index), True))
        write.writeFile()
        content = Content()
        read = Read("data/Proyecto1.txt", content)
        read.readFile()
        content.printAll()
        content.updateAvaibles(oldContent)
        write = Write("data/Availables.txt", content.stringLLate(content.availables))
        write.writeFile()
    elif option == '102':
        oldContent = content
        index = input("\n***** Insert index to delete a record: *****\n")
        content.deleteRecord(int(index))
        write = Write("data/Proyecto1.txt", content.stringLLate(content.records))
        write.writeFile()
        content = Content()
        read = Read("data/Proyecto1.txt", content)
        read.readFile()
        content.printAll()
        content.updateAvaibles(oldContent)
        write = Write("data/Availables.txt", content.stringLLate(content.availables))
        write.writeFile()
    elif option == '200':
        content.printAvaibles()
    elif option == '201':
        content.printAvaibles()
