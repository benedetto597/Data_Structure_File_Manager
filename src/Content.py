#-*- coding:utf8 -*-
from re import L
from src.LinkedList import LinkedList
from tabulate import tabulate

class Record:
    def __init__(self, value, avaible, type):
        self.value = value
        self.avaible = avaible
        self.type = type
        
class Content:
    def __init__(self):
        self.records = LinkedList()
        self.availables = LinkedList()
        self.deleted = LinkedList()
        self.freeSpace = None
        
    def addRecord(self, index, value):
        record = Record(value, self.setAvaible(value), self.setType(value))
        self.records.add(index, record)
        
    def addRecordInPosition(self, record, position):
        self.records.addInPosition(record, position)

    def printAll(self):
        print("="*43)
        print(tabulate(self.tabuLLate(self.records), headers="firstrow", tablefmt='psql'))
        print("="*43)
        
    def printDetail(self, index):
        print("="*43)
        record = [["Index", "Value", "Avaible", "Type"]]
        data = [
                self.records.getInPosition(int(index)).index, 
                self.records.getInPosition(int(index)).record.value,
                self.records.getInPosition(int(index)).record.avaible,
                self.records.getInPosition(int(index)).record.type
                ]
        record.append(data)
        print(tabulate(record, headers="firstrow", tablefmt='psql'))
        print("="*43)
        
    def tabuLLate(self, linkedList):
        records = [["Index", "Value", "Avaible", "Type"]]
        last = linkedList.getLast()
        
        for index in range(last.index):
            record = [
                        linkedList.getInPosition(index).index, 
                        linkedList.getInPosition(index).record.value,
                        linkedList.getInPosition(index).record.avaible,
                        linkedList.getInPosition(index).record.type
                    ]
            records.append(record)
        return records
        
    def setType(self, value):
        return "Text"
    
    def setAvaible(self, value):
        return True
    