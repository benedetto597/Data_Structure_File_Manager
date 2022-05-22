#-*- coding:utf8 -*-
import re as r
from src.LinkedList import LinkedList
from tabulate import tabulate

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
        record = Record(value, self.setAvaible(value), self.setType(value), len(value))
        self.records.add(index, record)
        
    def addRecordInPosition(self, index, value):
        record = Record(value, self.setAvaible(value), self.setType(value), len(value))
        self.records.addInPosition(record, index)
        
    def deleteRecord(self, index):
        self.records.deleteInPosition(index)

    def printAll(self):
        print("="*43)
        print(tabulate(self.tabuLLate(self.records), headers="firstrow", tablefmt='psql'))
        print("="*43)
        
    def printDetail(self, index):
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
        
    def stringLLate(self, linkedList, newIndex=None, inPos=False):
        records = ""
        lastIndex = linkedList.getLast().index   
        current = linkedList.getFirst()
        newRecord = False
        while current.next:
            records += current.record.value + "\n"
            current = current.next
           
        records += current.record.value
        
        return records
        
    def tabuLLate(self, linkedList):
        records = [["Index", "Value", "Avaible", "Type", "Len"]]
        last = linkedList.getLast()
        
        for index in range(last.index + 1):
            record = [
                        linkedList.getInPosition(index).index, 
                        linkedList.getInPosition(index).record.value,
                        linkedList.getInPosition(index).record.avaible,
                        linkedList.getInPosition(index).record.type,
                        linkedList.getInPosition(int(index)).record.len
                    ]
            records.append(record)
        return records
        
    def setType(self, value):
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
        return True
    