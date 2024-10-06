class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def predata(self, array):
        for data in array:
            newNode = Node(data)
            if self.headNode is None:
                self.headNode = newNode
                cur = self.headNode
            else:
                cur.nextNode = newNode
                cur = cur.nextNode

    def append(self, data):
        newNode = Node(data)
        if self.headNode is None:
            self.headNode = newNode
            return

        cur = self.headNode
        while cur.nextNode:
            cur = cur.nextNode
        cur.nextNode = newNode

    def addBtwNode(self, dataBefore, newData, dataAfter):
        cur = self.headNode
        while cur is not None:
            if cur.data == dataBefore and cur.nextNode and cur.nextNode.data == dataAfter:
                newNode = Node(newData)
                newNode.nextNode = cur.nextNode
                cur.nextNode = newNode
                return
            cur = cur.nextNode
        print(f"Nodes with values {dataBefore} and {dataAfter} not found consecutively.")

    def makeNewHeadNode(self, newHeadNode):
        newNode = Node(newHeadNode)
        newNode.nextNode = self.headNode
        self.headNode = newNode

    def printLinkedList(self):
        cur = self.headNode
        while cur is not None:
            print(cur.data)
            cur = cur.nextNode