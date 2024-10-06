class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    # Add data to the linked list
    def predata(self, array):
        for data in array:
            newNode = Node(data)
            if self.headNode is None:
                self.headNode = newNode
                cur = self.headNode
            else:
                cur.nextNode = newNode
                cur = cur.nextNode

    # Append data to the linked list
    def appendNode(self, data):
        newNode = Node(data)
        if self.headNode is None:
            self.headNode = newNode
            return

        cur = self.headNode
        while cur.nextNode:
            cur = cur.nextNode
        cur.nextNode = newNode

    # Append multiple data to the linked list
    def appendNodeArr(self, data):
        for i in data:
            newNode = Node(i)
            if self.headNode is None:
                self.headNode = newNode
            else:
                cur = self.headNode
                while cur.nextNode:
                    cur = cur.nextNode
                cur.nextNode = newNode
        return newNode

    # Add data between two nodes
    def addBtwNode(self, dataBefore, newData, dataAfter):
        cur = self.headNode
        while cur is not None:
            if cur.data == dataBefore and cur.nextNode.data == dataAfter:
                newNode = Node(newData)
                newNode.nextNode = cur.nextNode
                cur.nextNode = newNode
                return
            cur = cur.nextNode
        print(f"Nodes with values {dataBefore} and {dataAfter} not found consecutively.")

    # Make a new head node
    def makeNewHeadNode(self, newHeadNode):
        newNode = Node(newHeadNode)
        newNode.nextNode = self.headNode
        self.headNode = newNode

    # Print the linked list
    def printLinkedList(self):
        cur = self.headNode
        while cur is not None:
            print(cur.data)
            cur = cur.nextNode