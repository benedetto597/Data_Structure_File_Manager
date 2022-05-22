#-*- coding:utf8 -*-
import re as r
from src.LinkedList import LinkedList
from tabulate import tabulate

class Availables:
    def __init__(self, currIndex, value, lastIndex):
        self.currIndex = currIndex
        self.value = value
        self.lastIndex = lastIndex
class Record:
    def __init__(self, value, avaible, type, len):
        self.value = value
        self.avaible = avaible
        self.type = type
        self.len = len
        
class Content:
    def __init__(self):
        self.records = LinkedList()
        self.availables = LinkedList()
        self.deleted = LinkedList()
        self.freeSpace = None
        
    def addRecord(self, index, value):
        """ Agregar un nuevo registro al final """
        record = Record(value, self.setAvaible(value), self.setType(value), len(value))
        self.records.add(index, record)
        
    def addRecordInPosition(self, index, value):
        """ Agregar un nuevo registro en una posicion especifica """
        record = Record(value, self.setAvaible(value), self.setType(value), len(value))
        lastIndex = self.records.getLast().index
        if index > lastIndex:
            self.records.add(index, record)
        else:
            self.records.addInPosition(record, index)
        
    def deleteRecord(self, index):
        """ Eliminar un registro """
        self.records.deleteInPosition(index)

    def printAll(self):
        """ Imprimir todos los registros """
        print("="*43)
        print(tabulate(self.tabuLLateAll(self.records), headers="firstrow", tablefmt='psql'))
        print("="*43)
        
    def printDetail(self, index):
        """ Imprimir un registro en especifico """
        print("="*43)
        record = [["Index", "Value", "Avaible", "Type", "Len"]]
        data = [
                self.records.getInPosition(int(index)).index, 
                self.records.getInPosition(int(index)).record.value,
                self.records.getInPosition(int(index)).record.avaible,
                self.records.getInPosition(int(index)).record.type,
                self.records.getInPosition(int(index)).record.len
                ]
        record.append(data)
        print(tabulate(record, headers="firstrow", tablefmt='psql'))
        print("="*43)
    
    def printAvaibles(self):
        """ Imprimir todos los registros disponibles con su indice en el archivo origen """
        print("="*43)
        print(tabulate(self.tabuLLateAvailables(), headers="firstrow", tablefmt='psql'))
        print("="*43)
        
    def tabuLLateAvailables(self):
        """ Tabular todos los registros disponibles para imprimir """
        records = [["Index", "Last Index", "Value"]]
        last = self.availables.getLast()
        for index in range(last.index + 1):
            record = [
                        self.availables.getInPosition(index).record.currIndex, 
                        self.availables.getInPosition(index).record.lastIndex,
                        self.availables.getInPosition(index).record.value
                    ]
            records.append(record)
        return records
        
    def stringLLate(self, linkedList, newIndex=None, inPos=False):
        """ Convertir en texto todos los registros para escribir en archivo texto plano """
        records = ""
        lastIndex = linkedList.getLast().index   
        current = linkedList.getFirst()
        newRecord = False
        while current.next:
            records += current.record.value + "\n"
            current = current.next
           
        records += current.record.value
        
        return records
        
    def tabuLLateAll(self, linkedList):
        """ Tabular todos los registros para imprimir """
        records = [["Index", "Value", "Available", "Type", "Len"]]
        last = linkedList.getLast()
        
        for index in range(last.index + 1):
            record = [
                        linkedList.getInPosition(index).index, 
                        linkedList.getInPosition(index).record.value,
                        linkedList.getInPosition(index).record.avaible,
                        linkedList.getInPosition(index).record.type,
                        linkedList.getInPosition(index).record.len
                    ]
            records.append(record)
        return records
        
    def setType(self, value):
        """ Asignar un tipo de dato a partir de expresiones regulares """
        if r.match("^[0-9]*$", value):
            return "Int Number"
        # Expresion regular para numeros flotantes
        elif r.match("^[0-9]*\.[0-9]*$", value):
            return "Float Number"
        elif r.match("^[a-zA-Z]*$", value):
            return "String"
        elif r.match("^[a-zA-Z0-9_]*$", value):
            return "Alphanumeric"
        # Expresion regular para fechas
        elif r.match("^[0-9]{4}[\-\. \t][0-9]{2}[\-\. \t][0-9]{2}$$", value):
            return "Date"
        else:
            return "Other"
        
    def setAvaible(self, value):
        """ Asignar un registro disponible """
        return True
    
    def updateAvaibles(self, content):
        """ Actualizar la lista de disponibles """
        availables = self.records
        current = availables.getFirst()
        while current:
            beforeCurrent = content.records.getFirst()
            while beforeCurrent:
                if current.record.avaible == False:
                    availables.deleteInPosition(current.index)
                if current.record.value == beforeCurrent.record.value:
                    self.availables.add(current.index, Availables(current.index, current.record.value, beforeCurrent.index))
                beforeCurrent = beforeCurrent.next
            current = current.next
            
            
        
    