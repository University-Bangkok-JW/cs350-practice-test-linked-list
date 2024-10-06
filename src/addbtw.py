import cls

# Import the Node and SLinkedList classes from cls.py
Node = cls.Node
SLinkedList = cls.SLinkedList

# Create an SLinkedList object
list = SLinkedList()

# Our array to be added to the linked list
array = [1, 2, 3, 4, 6]

for data in array:
    newNode = Node(data)
    if list.headNode is None:
        list.headNode = newNode
        cur = list.headNode
    else:
        cur.nextNode = newNode
        cur = cur.nextNode

list.addBtwNode(4, 5, 6)

list.printLinkedList()