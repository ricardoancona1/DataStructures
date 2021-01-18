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


