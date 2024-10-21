class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

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
                cur.next = newNode
                cur = cur.next

    # Append data to the linked list
    def appendNode(self, data):
        newNode = Node(data)
        if self.headNode is None:
            self.headNode = newNode
            return

        cur = self.headNode
        while cur.next:
            cur = cur.next
        cur.next = newNode

    # Append multiple data to the linked list
    # Reuse the appendNode method
    def appendNodeArr(self, data):
        for i in data:
            self.appendNode(i)

    # Add data between two nodes
    def addBtwNode(self, dataBefore, newData, dataAfter):
        cur = self.headNode
        while cur is not None:
            if cur.data == dataBefore and cur.next.data == dataAfter:
                newNode = Node(newData)
                newNode.next = cur.next
                cur.next = newNode
                return
            cur = cur.next
        print(f"Nodes with values {dataBefore} and {dataAfter} not found consecutively.")

    def delNode(self, data):
        cur = self.headNode

        if cur is None:
            print("List is empty.")
            return

        prev = None
        while cur is not None and cur.data != data:
            prev = cur
            cur = cur.next

        if cur is None:
            print(f"Node with data {data} not found.")
            return

        prev.next = cur.next

    # Make a new head node
    def makeNewHeadNode(self, newHeadNode):
        newNode = Node(newHeadNode)
        newNode.next = self.headNode
        self.headNode = newNode

    # Print the linked list
    def printLinkedList(self):
        cur = self.headNode
        while cur is not None:
            print(cur.data)
            cur = cur.next