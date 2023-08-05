class Node:
    def __init__(self,row,col,val):
        self.id = str(row)+'-'+str(col)
        self.col = col
        self.row = row
        self.val = val
        self.distanceFromStart  = float('inf')
        self.estimateDistance = float('inf')
        self.cameFrom = None

def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):  
    
    nodes = initializeNodes(graph)  # Corrected function name

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.distanceFromStart = 0
    startNode.estimateDistance = manhattendistance(startNode, endNode)

    nodeToVisit = MinHeap([startNode])

    while not nodeToVisit.isEmpty():
        print(nodeToVisit.nodePositionInHeap)
        currentMinDistance = nodeToVisit.remove()
        if currentMinDistance == endNode:
            break

        neighbors = getNeighbhors(currentMinDistance, nodes)

        for neighbor in neighbors:

            if neighbor.val == 1:
                continue

            tentativeDistance = currentMinDistance.distanceFromStart + 1

            if tentativeDistance >= neighbor.distanceFromStart:
                continue
            neighbor.distanceFromStart = tentativeDistance
            neighbor.estimateDistance = tentativeDistance+manhattendistance(neighbor, endNode)
            neighbor.cameFrom = currentMinDistance
            if not nodeToVisit.contain(neighbor):
                nodeToVisit.insert(neighbor)
            else:
                nodeToVisit.update(neighbor)
                

    return reconstructPath(endNode)

# Rest of the code remains the same...


# Rest of the code remains the same...


def reconstructPath(endNode):
    if not endNode.cameFrom:
        return []
    
    path = []
    currentNode = endNode
    while currentNode:
        path.append([currentNode.row,currentNode.col])
        currentNode = currentNode.cameFrom
    
    return path[::-1]
    




def getNeighbhors(currentNode,nodes):
    neighbors = []
    numRows = len(nodes)
    numcols = len(nodes[0])
    currentRow = currentNode.row
    currentCol = currentNode.col
    if currentRow < numRows - 1:
        neighbors.append(nodes[currentRow +1][currentCol])
    if currentRow > 0:
        neighbors.append(nodes[currentRow-1][currentCol])
    if currentCol < numcols - 1:
        neighbors.append(nodes[currentRow][currentCol+1])
    if currentCol > 0:
        neighbors.append(nodes[currentRow][currentCol -1])
  
    return neighbors
 

def manhattendistance(startNode,endNode):
    return abs(startNode.row - endNode.row) + abs(startNode.col - endNode.col)


def initializeNodes(graph):  # Fixed function name
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, val in enumerate(row):
            nodes[i].append(Node(i, j, val))
    return nodes
                  
class MinHeap:
    def __init__(self,array):
        self.nodePositionInHeap = {node.id : i for i ,node in enumerate(array)}
        self.heap = self.buildHeap(array)

    def buildHeap(self,array):
        parent = len(array) // 2 - 1
        for current in reversed(range(parent)):
            self.siftDown(current,len(array)- 1,array)
        return array
    
    def siftDown(self,current,endId,heap):
        childOne = current * 2 + 1
        while childOne <= endId:
            childTwo = current * 2 + 2 if current * 2 + 2 <=endId else -1
            if childTwo != -1 and heap[childOne].estimateDistance < heap[childTwo].estimateDistance:
                idxswap = childOne
            else:
                idxswap = childTwo
            if heap[idxswap].estimateDistance < heap[current].estimateDistance:
                self.swap(current,idxswap,heap)
                current = idxswap
                childOne = idxswap
                childOne = current * 2 + 1
            else:
                return
            
    def siftUp(self,current,heap):
        parent = (current - 1) // 2
        while current > 0 and heap[current].estimateDistance < heap[parent].estimateDistance:
                self.swap(current,parent,heap)
                current = parent
                parent = (current - 1) // 2
    
    def isEmpty(self):
        return len(self.heap) == 0
    def remove(self):
        self.swap(0,len(self.heap) - 1,self.heap)
        node = self.heap.pop()
        del self.nodePositionInHeap[node.id]
        self.siftDown(0,len(self.heap)-1,self.heap)
        return node
            
    def insert(self,node):
        self.heap.append(node)
        self.nodePositionInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) -1, self.heap)

    def swap(self,node1,node2,heap):
        self.nodePositionInHeap[heap[node1].id] = node2
        self.nodePositionInHeap[heap[node2].id] = node1
        heap[node1],heap[node2] = heap[node2],heap[node1]
    
    def update(self,node):
        self.siftUp(self.nodePositionInHeap[node.id],self.heap)

    def contain(self,node):
        return node in self.nodePositionInHeap
    
graph = [[0,0,0,0,0],
         [0,1,1,1,0],
         [0,0,0,0,0],
         [1,0,1,1,1],
         [0,0,0,0,0]]
lis = aStarAlgorithm(0, 1, 4, 3, graph)
print(lis)



            


    
