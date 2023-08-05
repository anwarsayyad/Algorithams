class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.len = 0

    def push(self,value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
            self.len += 1
            return True
        
        new_node.next = self.top
        self.top = new_node
        self.len += 1

    def pop(self):
        if self.len == 0:
            return None
        
        if self.len == 1:
            self.top = None
            self.len -= 1

        temp = self.top
        self.top = temp.next
        temp.next = None
        self.len -= 1

    def prin_s(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()
        print('length ' +' : ',self.len)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)

s.prin_s()
s.pop()

s.prin_s()
s.pop()

s.prin_s()
s.pop()

s.prin_s()
s.pop()

s.prin_s()
s.pop()
        
