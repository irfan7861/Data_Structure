# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None

# class SLinkedList:
#     def __init__(self):
#         self.headval = None

# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# # Link first Node to second node
# list1.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3
# e4 = e3

# print(e3.dataval)

# ####### Traversing a Linked List

# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None

# class SLinkedList:
#     def __init__(self):
#         self.headval = None

#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print (printval.dataval)
#             printval = printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# # Link first Node to second node
# list.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3

# list.listprint()

# # Node of a doubly linked list 
# class Node:
#     def __init__(self, next=None, prev=None, data=None):
#         self.next = next # reference to next node in DLL
#         self.prev = prev # reference to previous node in DLL
#         self.data = data

# # Adding a node at the front of the list
# def push(self, new_data):
 
#     # 1 & 2: Allocate the Node & Put in the data
#     new_node = Node(data = new_data)
 
#     # 3. Make next of new node as head and previous as NULL
#     new_node.next = self.head
#     new_node.prev = None
 
#     # 4. change prev of head node to new node 
#     if self.head is not None:
#         self.head.prev = new_node
 
#     # 5. move the head to point to the new node
#     self.head = new_node 



#     # Python program to demonstrate 
# # circular linked list traversal 

# # Structure for a Node
# class Node:
	
# 	# Constructor to create a new node
# 	def __init__(self, data):
# 		self.data = data 
# 		self.next = None

# class CircularLinkedList:
	
# 	# Constructor to create a empty circular linked list
# 	def __init__(self):
# 		self.head = None

# 	# Function to insert a node at the beginning of a
# 	# circular linked list
# 	def push(self, data):
# 		ptr1 = Node(data)
# 		temp = self.head
		
# 		ptr1.next = self.head

# 		# If linked list is not None then set the next of
# 		# last node
# 		if self.head is not None:
# 			while(temp.next != self.head):
# 				temp = temp.next
# 			temp.next = ptr1

# 		else:
# 			ptr1.next = ptr1 # For the first node

# 		self.head = ptr1 

# 	# Function to print nodes in a given circular linked list
# 	def printList(self):
# 		temp = self.head
# 		if self.head is not None:
# 			while(True):
# 				print "%d" %(temp.data),
# 				temp = temp.next
# 				if (temp == self.head):
# 					break


# # Driver program to test above function

# # Initialize list as empty
# cllist = CircularLinkedList()

# # Created linked list will be 11->2->56->12
# cllist.push(12)
# cllist.push(56)
# cllist.push(2)
# cllist.push(11)

# print "Contents of circular Linked List"
# cllist.printList()
		
# # This code is contributed by 



class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next
        self.prev = prev
        self.data = data

def push(self, new_data):
    new_node = Node(data= new_data)
    new_node.next = self.head
    new_node.prev = None        


    if self.head is not None:
        self.head.prev = new_node
    self.head = new_node    


e1 = Node()
e1.head = Node("abc")

print(e1.head.data)































        