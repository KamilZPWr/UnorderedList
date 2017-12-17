from UnorderedList import UnorderedList as ul

class Deque:
    def __init__(self):
        self.items=ul()

    def isEmpty(self):
        return self.items.isEmpty()

    def addFront(self,item):
        self.items.add(item)

    def addRear(self,item):
        l=self.items.size()
        self.items.insert(item,l)

    def removeFront(self):
        return( self.items.pop(1))

    def removeRear(self):
        l=self.items.size()
        return( self.items.pop(l))
        
    def size(self):
        return self.items.size()

s=Deque()
s.addFront(12)
s.addFront('t')
s.addRear(0)
s.addRear(43)
print(s.size())
print(s.removeFront())
print(s.removeRear())
