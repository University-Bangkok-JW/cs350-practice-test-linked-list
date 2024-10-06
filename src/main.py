import cls

# Import the Node and SLinkedList classes from cls.py
Node = cls.Node
SLinkedList = cls.SLinkedList

# Pre data to be added to the linked list
array = [1, 2, 3, 4, 5]

# Create an SLinkedList object
list = SLinkedList()

list.predata(array)

# Print the linked list
list.printLinkedList()