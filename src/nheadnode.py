import cls

# Import the Node and SLinkedList classes from cls.py
Node = cls.Node
SLinkedList = cls.SLinkedList

# Create an SLinkedList object
list = SLinkedList()

# Our array to be added to the linked list
array = [2, 3, 4, 5, 6]

list.predata(array)

# print the linked list
print("Original Linked List:")
list.printLinkedList()

# --------------------------------------------

newHeadNode = 1
list.makeNewHeadNode(newHeadNode)

# print the linked list
print("\nLinked List after making new head node:")
list.printLinkedList()