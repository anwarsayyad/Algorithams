class Test:
    def __init__(self):
        pass

    def getMin(self,array) -> int:
            
            lp = len(array) // 2 - 1
            for current in reversed(range(lp)):
                self.shiftDown(current,len(array) - 1, array)
            print(array)
            return array[0]

    def shiftDown(current,end,heap):
        childOne = current * 2 + 1
        while childOne <= end:
            childTwo = current * 2 + 2 if current * 2 + 2 <= end else -1
            if childTwo != -1 and heap[childOne] < heap[childTwo]:
                ids = childOne
            else:
                ids = childTwo
            if heap[ids] < heap[current]:
                heap[ids],heap[current] = heap[current],heap[ids]
                current = ids
                childOne = current * 2 + 1
            else:
                return
t = Test
print(t.getMin([5,7,8,9,0]))