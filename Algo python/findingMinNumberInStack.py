class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MinStack:

    def __init__(self):
        self.topi = None
        self.heap = []
        

    def push(self, val: int) -> None:
        new_Node = Node(val)
        self.heap.append(val)
        if self.topi == None:
            self.topi = new_Node
            return None
        new_Node.next = self.topi
        self.topi = new_Node
        current = len(self.heap) - 1
        while current > 0:
            parent = current // 2
            if self.heap[parent] > self.heap[current]:
                self.heap[current],self.heap[parent] = self.heap[parent],self.heap[current]
            current = parent

    def pop(self) -> None:
        if self.topi == None:
            return None

        if self.topi.val == self.heap[0]:
            self.heap[0],self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1],self.heap[0]
            self.heap.pop()
            current = 0
            left = current * 2 + 1
            while left < len(self.heap) -1:
                right = current * 2 + 2 if current * 2 + 2 < len(self.heap) - 1 else -1 
                if right != -1 and self.heap[left] > self.heap[right]:
                    ids = right
                else:
                    ids = left
                if self.heap[current] > self.heap[ids]:
                    self.heap[ids],self.heap[current] = self.heap[current],self.heap[ids]
                    current = ids
                    left = current * 2 + 1
        self.topi = self.topi.next


    def top(self) -> int:
        min = self.topi.val 
        return min

    def getMin(self) -> int:
        return self.heap[0]
    
m = MinStack()
m.push(512)
m.push(-1024)
m.push(-1024)
m.push(512)
print(m.getMin())
m.pop()
print(m.getMin())
m.pop()
print(m.getMin())