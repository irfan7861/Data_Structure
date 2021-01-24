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
# list.listprint()
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

# Link first Node to second node
# list.headval.nextval = e2

# Link second Node to third node
# e2.nextval = e3

# list.listprint()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None;
class Linkedlist:
    def __init__(self):
        self.start = None;  
        def insertlast(self,value):
            newnode=Node(value)
            if(self.start==None)
                self.start=newnode;
            else:
                temp=self.start    





# A simple Python program to introduce a linked list 

# Node class 
class Node: 

	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 


# Linked List class contains a Node object 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None


# Code execution starts here 
if __name__=='__main__': 

	# Start with the empty list 
	llist = LinkedList() 

	llist.head = Node(1) 
	second = Node(2) 
	third = Node(3) 

	''' 
	Three nodes have been created. 
	We have references to these three blocks as head, 
	second and third 

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | None |	 | 2 | None |	 | 3 | None | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

	llist.head.next = second; # Link first node with second 

	''' 
	Now next of first Node refers to second. So they 
	both are linked. 

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | o-------->| 2 | null |	 | 3 | null | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

	second.next = third; # Link second node with the third node 

	''' 
	Now next of second Node refers to third. So all three 
	nodes are linked. 

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | o-------->| 2 | o-------->| 3 | null | 
	+----+------+	 +----+------+	 +----+------+ 
	'''
