class Queue:
    queueSize = 5
    queue = [None]*queueSize  # Define array lenght of 5
    front = -1
    rear = -1

    def printQueue():
        print(Queue.queue)

    def isQueueEmpty():
        if Queue.front == -1 and Queue.rear == -1:
            return True
        else:
            return False

    def isQueueFull():
        if Queue.rear == Queue.queueSize-1:
            return True
        else:
            return False
    def printPointers():
        print("Rear= ",Queue.rear, " Front= ", Queue.front)

    def enqueueElement():
        if Queue.isQueueFull():
            print("Sorry queue is full")
        else:
            if Queue.front==-1:
                Queue.front=0
            inputValue = input("Please input a value to enqueue ")
            Queue.rear = Queue.rear+1
            Queue.queue[Queue.rear] = inputValue
            Queue.printPointers()
            

    def dequeueElement():
        if Queue.isQueueEmpty():
            print("Sorry, Queue is empty")

        else:
            if Queue.front == Queue.rear:
                Queue.front = Queue.rear = -1
            else:
                Queue.front = Queue.front+1

        Queue.printPointers()
        """ in case you need to remove the element from the queue
            for i in range(0,Queue.queueSize-1):
                Queue.queue[i]=Queue.queue[i+1]
            Queue.rear=Queue.rear-1
        print(Queue.rear," ",Queue.front)
        """
    def printMenu():
        print("Please input  \n1.-Enqueue \n2.-Dequeue \n3.-Exit")
        inputOption = input()
        return int(inputOption)


print("Welcome to the Queue software")
while True:
    inputOption = Queue.printMenu()
    if inputOption == 1:
        Queue.enqueueElement()
    elif inputOption == 2:
        Queue.dequeueElement()
    elif inputOption == 3:
        print("bye, come back anytime :)")
        break
    else:
        print("Sorry wrong input")

