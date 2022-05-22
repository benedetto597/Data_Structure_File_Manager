#-*- coding:utf8 -*-
class Node:
    def __init__(self, index, record):
        self.index = index
        self.record = record
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, index, record):
        if not self.first:
            self.first = Node(index, record)
            return True
        else: 
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(index, record)
            return True
        return False

    def addInPosition(self, record, position):
        count = 0
        if position == 0:
            queue = self.first
            self.first = Node(position, record)
            self.first.next = queue
            return True
        else:
            if position > 0:
                current = self.first
                before = self.first
                while current.next:
                    current = current.next
                    count = count +1
                    if count == position:
                        before.next = Node(position, record)
                        before.next.next = current
                        return True
                    before = before.next
        return False
    
    def delete(self, record):
        prev = None
        current = self.first
        if self.first is None:
            return False
        else:
            while (current.record != record and current.next is not None):
                prev = current
                current = current.next
            if(current.record == record):
                if current == self.first:
                    if current.next is None:
                        self.first = None
                    else:
                        self.first = current.next
                else:
                    if current.next is None:
                        prev.next = None
                    else:
                        prev.next = current.next
            else:
                return False
            
    def deleteInPosition(self, position):
        count = 0
        if position == 0:
            queue = self.first
            self.first = queue.next
            return True
        else:
            if position > 0:
                current = self.first
                before = self.first
                while current.next:
                    current = current.next
                    count = count +1
                    if count == position:
                        before.next = current.next
                        return True
                    before = before.next
        return False

    def getFirst(self):
        return self.first

    def getLast(self):
        last = self.first
        while last.next:
            last = last.next
        return last

    def getInPosition(self, position):
        count = 0
        if position == 0:
            return self.first
        else:
            if position > 0:
                current = self.first
                before = self.first
                while current.next:
                    current = current.next
                    count = count + 1
                    if count == position:
                        return current
                    before = before.next
        return False

    def printLL(self):
        current = self.first
        while current.next:
            print(current.record)
            current = current.next
        print(current.record)