class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node('Sila by SUD')
print(node1.data)
head = None

def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    if (head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode

def traverseLinkedList():
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
    else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode


def insertNodeAfterGivenNode(data, node):
    newNode = Node(data)
    global head

    if(head == None):
        head = newNode
    else:
        current = head
        prev = None

        while(current.data != node):
            prev = current
            current = current.next

            if(current == None):
                print('The node does not exist')
                return

    newNode.next = current
    prev.next = newNode

insertNodeAtTheBeginning('blue')
insertNodeAtTheBeginning('purple')
insertNodeAtTheEnd('red')
insertNodeAtTheEnd('black')
insertNodeAtTheEnd('white')
insertNodeAfterGivenNode('green')

traverseLinkedList()


