class Node:
    def_init_(self, data):
        self.data = data  
        self.next = None
        
    node1 = Node
    print (node1.data)
    head = node1

def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)
    
    if(head == None)
        head = newNode
    else:
        newNode.next = head
        head = newNode
def traverseLinKedList():
    current = head
    while(current):
        print(current.data, end=" -> ")
        current = current.next
        
        node1 = Node
        head = node1
        
insertNodeAtTheBeginning
traverseLink()

def insertNodeAtTheEnd(data):
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode
        
        

    
    
    
