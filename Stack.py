from UnorderedList import UnorderedList as ul

class Stack:
    def __init__(self):
        self.items=ul()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self,item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(1)

    def peek(self):
        l=self.items.size()
        print( self.items.show_item(-l))

    def size(self):
        return self.items.size()

s=Stack()
print(s.isEmpty())
s.push('t')
s.push(12)
s.push(5)
s.push(5)
s.push(5)
print(s.size())
s.push(5)
s.push(5)
s.push(5)
s.push(5)
s.push(7)
s.peek()
print(s.isEmpty())
print(s.pop())
print(s.size())

