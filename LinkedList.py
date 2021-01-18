class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
        
    #Common methods
    def getSize(self):
        count=0
        node=self.head
        while node:
            count+=1
            node=node.next
        return count
    def getFirst(self):
        return self.head
    
    def getLast(self):
        lastNode=self.head
        if lastNode:
            while(lastNode.next):
                lastNode=lastNode.next
        return lastNode
    
    def clear(self):
        self.head=None

def printMenu():
    print("Please input  \n1.-Print linked list size \n2.-Add a node \n3.-Print last node \n4.-Print first node")
    inputOption = input()
    return int(inputOption)

  
node= Node(input("Node1 :"))
node2=Node(input("Node2 :"))
node3=Node(input("Node3 :"))
node.next=node2
node2.next=node3
linkedlist=LinkedList(node)
print("First node:",linkedlist.head.next.data)
listSize=linkedlist.getSize()
print("Size of linked list",listSize)
firstNode=linkedlist.getFirst()
print("This is the first node ",firstNode.data)
lastNode=linkedlist.getLast()
print("this is the last node",lastNode.data)

linkedlist.clear()
print("Function to empty linked list was executed")
print("linked list size:",linkedlist.getSize())
